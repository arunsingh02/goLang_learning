# -*- coding:utf-8 -*-
from BeautifulSoup import BeautifulStoneSoup
import cgi
import re
import htmlentitydefs
import urllib2

class convert(object):
    def __init__(self):
        pass

    def get_clean_number_by_lang(self, lang, txt):
        lang = lang.upper()
        txt = ''.join(map(lambda x:x.strip(), txt.split(' ')))
        txt = txt.replace('&#8364;', '')
        txt = txt.replace('&#8217;', "'")
        minus_list = ['&#8212;', '&#8213;', '&#8722;', '&#8211;', '&#8212;']
        for each in minus_list:
            txt = txt.replace(each, '-')
        txt = re.sub("[a-zA-Z$%*']+", '', txt)
        if lang in ['E', 'ENGLISH']:
            txt = txt.replace(',', '')
        if lang in ['G', 'GERMAN']:
           txt = txt.replace('.', '')
           txt = txt.replace(',', '.')
        txt = txt.strip()
        if '(' and ')' in str(txt):
            txt = txt.replace('(', '').replace(')', '')
            txt = '-%s' % str(txt)
        else:
            txt = str(txt)
        txt = txt.strip()
        if txt in ['-']: txt = '0'
        txt = txt.replace("'", "")
        try:
           new_txt = int(txt)
        except:
           try:
               new_txt = float(txt)
           except:
              txt = ''
        return txt

    def HTMLEntitiesToUnicode1(self, text):
        def fixup(m):
            text = m.group(0)
            if text[:2] == "&#":
                # character reference
                try:
                    if text[:3] == "&#x":
                        return unichr(int(text[3:-1], 16))
                    else:
                        return unichr(int(text[2:-1]))
                except ValueError:
                    print "Value Error"
                    pass
            else:
                # named entity
                # reescape the reserved characters.
                try:
                    if text[1:-1] == "amp":
                        text = "&"
                    elif text[1:-1] == "gt":
                        text = ">"
                    elif text[1:-1] == "lt":
                        text = "<"
                    else:
                        print text[1:-1]
                        text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
                except KeyError:
                    print "keyerror"
                    pass
            return text # leave as is
        return re.sub("&#?\w+;", fixup, text)

    def HTMLEntitiesToUnicode(self, text):
        """Converts HTML entities to unicode.  For example '&amp;' becomes '&'."""
        text = unicode(BeautifulStoneSoup(text, convertEntities=BeautifulStoneSoup.ALL_ENTITIES))
        return text

    def unicodeToHTMLEntities(self, text):
        """Converts unicode to HTML entities.  For example '&' becomes '&amp;'."""
        text = cgi.escape(text).encode('ascii', 'xmlcharrefreplace')
        return text

    def convertNonAsciiToHTMLEntities(self, text):
        if not type(text) in [str, unicode]:
            text = str(text)
        text = text.replace('&amp;', '&')
        try:
            text = text.decode('utf-8', errors='ignore')
        except:
            print 'data error :[%s]' %text
            text = ''
        new_txt = ""
        error_flg = 0
        find_entities = {}
        for x in text:
            if ord(x)==ord('&'):
               new_txt += '&amp;'
            elif ord(x) < 128:
                new_txt += x
            else:
                flg = 0
                try:
                    elm =  self.unicodeToHTMLEntities(x)
                except:
                    flg = 1
                    elm = '&#'+str(ord(x))+';'
                if flg:
                   find_entities[elm] = 0
                new_txt += elm #self.unicodeToHTMLEntities(x)
        new_txt = new_txt.replace('&amp;#', '&#')
        new_txt = new_txt.replace('&amp;quot;', '&quot;')
        new_txt = new_txt.replace('&amp;quot;', '&quot;')
        new_txt = new_txt.replace('&#160;', ' ')
        new_txt = new_txt.replace('&#173;', '-')
        new_txt = new_txt.replace('%u2014', '-')
        new_txt = new_txt.replace('&#226;&#128;&#8221;', '-')
        new_txt = new_txt.replace('&#226;&#128;&#148;', '-')
        new_txt = new_txt.replace('&amp;', '&')
        new_txt = new_txt.replace('&#8212;', '-')
        new_txt = new_txt.replace('&#8220;', '"')
        new_txt = new_txt.replace('&#8217;', "'")
        new_txt = new_txt.replace('&#8221;', '"')
        new_txt = new_txt.replace('&#8211;', '-')
        cp1252_to_unicode_dict = {'&#92;':'&#2019;', '&#145;':'&#8216;', '&#146;':'&#8217;', '&#147;':'&#8220;', '&#148;':'&#8221;', '&#149;':'&#8226;', '&#150;':'&#8211;', '&#151;':'&#8212;', '&#152;':'&#732;', '&#153;':'&#8482;'}
        for k, v in cp1252_to_unicode_dict.items():
            new_txt = new_txt.replace(k, v)
            #try:
            # find_entities[k] = 1
        error_keys = []
        find_keys = find_entities.keys()
        for find_key in find_keys:
            flg = cp1252_to_unicode_dict.get(find_key, 0)
            if flg == 0:
               error_flg = 1
               error_keys.append(find_key)
               break
        if error_flg:
           pass
        new_txt = str(' '.join(new_txt.split()))
        return new_txt


if __name__ == '__main__':
    obj = convert()
    #text = "&amp;, &reg;, &lt;, &gt;, &cent;, &pound;, &yen;, &euro;, &sect;, &copy;"
    #uni = obj.HTMLEntitiesToUnicode1(text)
    #htmlent = obj.unicodeToHTMLEntities(uni)
    #txt = urllib2.unquote('%26%238212%3B')
    txt = obj.convertNonAsciiToHTMLEntities('AmeriCredit Automobile Receivables Trust 2013-3, or the issuing entity, or the trust, is a Delaware statutory trust. The issuing entity will issue the notes and be liable for their payment. The issuing entity\xe2\x80\x99s principal asset will be a pool of sub-prime automobile loan contracts secured by new and used automobiles, light duty trucks and vans.')
    #print txt
    txt = 'Increase (+)/decrease (\xe2\x80\x93) in trade payables and other liabilities not attributed to investing or financing activities'
    txt = 'Interest result \xe2\x80\x9cSchuldschein\xe2\x80\x9d'
    #txt = urllib2.unquote('')
    #txt = obj.get_clean_number_by_lang('ENGLISH', txt)
    #txt = 'in â¬ million'
    txt = obj.convertNonAsciiToHTMLEntities(txt)
    print 'txt: ', txt
    #print uni
    #print htmlent

####################################################################################


def get_clean_value_new(self, svalue):
        svalue = ''.join(svalue.strip().split())
        svalue = svalue.replace(';', '').replace('$ ', '').replace('$', '').replace('%', '').replace('&nbsp', '').replace('..', '.')
        if ('(' in svalue and ')' in svalue):
            ast = 'abcdefghijklmnopqrstuvwxyz'
            for e in ast:
                sb = '('+e+')'
                ss = '('+e.upper()+')'
                svalue = svalue.replace(ss, '')
                svalue = svalue.replace(sb, '')
        svalue = svalue.replace('&#162', '').replace('&#165', '').replace('&#65288', '(').replace('&#65289', ')').replace('&#65293', '').replace('&#12540', '').replace('&#163', '').replace('&#165', '')
        flip_sign = ''
        if ('(' in svalue and ')' in svalue) or (svalue.startswith('-') > 0):
            flip_sign = '-1'
        if '&#8208' in svalue:
            flip_sign = '-1'
        svalue = svalue.replace('&#8211', '').replace('\xe2\x80\x93', '').replace('&#8364', '').replace('&#8208', '').replace('&#8722', '').replace('&#8212', '').replace('&#160', '').replace('&#8213', '').replace('&#402', '')
        dot_count = 0
        new_string = ''
        for e in svalue:
            e = e.strip()
            if e in '0123456789':
               new_string += e
            elif e in '.':
               new_string += e
               dot_count = dot_count + 1
            else:
               continue

        if (dot_count > 1):
           return 0
        mul_factor = 1
        if flip_sign:
           mul_factor = -1
        try:
             if (dot_count == 1):
                 new_num = mul_factor*float(new_string)
             else:
                new_num = mul_factor*int(new_string)
        except:
             new_num = 0
        return new_num

####################################################################################

def arrange_order_ph(order_phs):
            order_phs       = list(set(order_phs))
            order_phs.sort()
            order_phs       = map(lambda x:str(x[1]), order_phs)
            new_order_phs   = []
            for ph in order_phs:
                if ph in new_order_phs:continue
                new_order_phs.append(ph)
            order_phs       = new_order_phs[:]
            pt_order        = ['Q1', 'Q2', 'H1', 'Q3', 'M9', 'Q4', 'H2', 'FY']
            ph_dict         = {}
            for ph in order_phs:
                p   = int(ph[2:])
                pt  = ph[:2]
                if p not in ph_dict:
                    ph_dict[p] = []
                mtup    = (pt_order.index(pt), pt)
                ph_dict[p].append(mtup)
            order_phs   = []
            for period in sorted(ph_dict.keys()):
                pt_lst  = ph_dict[period]
                pt_lst.sort()
                for pt_tup in pt_lst:
                    ph  = pt_tup[1] + str(period)
                    order_phs.append(ph)
            self.historical_phs  = order_phs[:]
            return order_phs
