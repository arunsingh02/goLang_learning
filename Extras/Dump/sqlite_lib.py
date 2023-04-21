import sqlite3
from sqlite3 import Error
import sys

class sqLiteApi(object):

    def __init__(self):
        pass

    def create_connection(self, db_file):
        try:
            conn = sqlite3.connect(db_file, timeout=30000)
            return conn
        except Error as e:
            print('Connection Error:', e)
        return None


    def createLiteTable(self, conn, cur, db_file, table_name, column_list):
        if (not conn) or (not cur):
            conn = self.create_connection(db_file)
            cur  = conn.cursor()

        if not column_list:
            return 'error'

        column_str  = '(' +       ', '.join([x[0] + ' ' +x[1] for x in column_list])        + ')'

        stmt = 'CREATE TABLE IF NOT EXISTS ' + table_name +  '' + column_str
        cur.execute(stmt)
        return 'done'

    def readFromLiteComplex(self, conn, cur, db_file, stmt):
        if (not conn) or (not cur):
            conn = self.create_connection(db_file)
            cur  = conn.cursor()
        cur.execute(stmt)
        rows = cur.fetchall()
        return rows

    def readFromLite(self, conn, cur, db_file, table_name, column_list, condition=''):
        if (not conn) or (not cur):
            conn = self.create_connection(db_file)
            cur  = conn.cursor()

        column_str  = '*' if(not column_list) else  ','.join(column_list)
        if condition:
            stmt = 'SELECT ' + column_str + ' FROM ' + table_name + ' where '+ condition
        else:
            stmt = 'SELECT ' + column_str + ' FROM ' + table_name
        rows = []
        try:
            cur.execute(stmt)
            rows = cur.fetchall()
        except Exception as e:
            #print e
            pass
        return rows

    def readFromLiteDefault(self, conn, cur, db_file, table_name, column_list, condition=''):
        if (not conn) or (not cur):
            conn = self.create_connection(db_file)
            cur  = conn.cursor()

        column_str  = '*' if(not column_list) else  ','.join(column_list)
        if condition:
            stmt = 'SELECT ' + column_str + ' FROM ' + table_name + ' where '+ condition
        else:
            stmt = 'SELECT ' + column_str + ' FROM ' + table_name
        #print stmt
        rows    = []
        try:
            cur.execute(stmt)
            rows = cur.fetchall()
        except:
            pass
        return rows

    def updateToLite(self, conn, cur, db_file, table_name, set_tup_list, condition):
        if (not conn) or (not cur):
            conn = self.create_connection(db_file)
            cur  = conn.cursor()

        with conn:
            if not set_tup_list:
                print 'Error: Empty Data Supplied'
                return 'error'
            parsed_list = map(lambda s: (s[0], str(s[1])) if (not isinstance(s[1], str)) else (s[0], '"'+str(s[1])+'"'), set_tup_list)
            set_str = ', '.join([''.join((s[0], '=', s[1])) for s in parsed_list])
            if condition:
                stmt = 'UPDATE ' + table_name +  ' SET  ' + set_str + ' where '+ condition
            else:
                stmt = 'UPDATE ' + table_name +  ' SET  ' + set_str
            #print 'SQL-STATEMENT - ', stmt
            cur.execute(stmt)
        return 'done'

    def updateToLiteQuery(self, conn, cur, db_file, stmt):
        if (not conn) or (not cur):
            conn = self.create_connection(db_file)
            cur  = conn.cursor()

        with conn:
            #print stmt
            cur.execute(stmt)
        return 'done'

    def insertIntoLite(self, conn, cur, db_file, table_name, column_tup, value_list):
        if (not conn) or (not cur):
            conn = self.create_connection(db_file)
            cur  = conn.cursor()
        with conn:
            if not value_list:
                #print 'Error: Trying to insert Empty rows'
                return 'error'

            value_str   = ', '.join([str(x_tup) for x_tup in value_list])
            if len(value_list[0]) == 1:
                value_str   = '(\"' + str(value_list[0])+ '\")'

            column_str  = str(column_tup)
            if len(column_tup) == 1:
                column_str  = '(' + str(column_tup[0]) + ')'

            stmt = 'INSERT INTO ' + table_name +  ' ' + column_str + ' VALUES  ' + value_str
            #print stmt
            cur.execute(stmt)
        return 'done'

    def deleteSQLite(self, conn, cur, db_file, table_name, condition=''):
        if (not conn) or (not cur):
            conn = self.create_connection(db_file)
            cur  = conn.cursor()

        with conn:
            if condition:
                stmt = 'delete from ' + table_name + ' where '+condition
            else:
                stmt = 'delete from ' + table_name
            #print stmt
            cur.execute(stmt)
            conn.commit()
        return 'done'


    def dropTable(self, conn, cur, db_file, table_name):
        if (not conn) or (not cur):
            conn = self.create_connection(db_file)
            cur  = conn.cursor()
        with conn:
            stmt = 'drop table ' + table_name
            cur.execute(stmt)
        return 'done'


    def copyFromDiffDatabase(self, conn, cur, db_file, db_file2, table_name1, table_name2, column_list, condition=''):
        if (not conn) or (not cur):
            conn = self.create_connection(db_file)
            cur  = conn.cursor()

        with conn:
            stmt = 'delete from ' + table_name1 + ' where '+condition
            #print stmt
            cur.execute(stmt)

            stmt = 'ATTACH \"'+ db_file2 + '\" as BM'
            #print stmt
            cur.execute(stmt)

            column_str  = '*' if(not column_list) else  ','.join(column_list)
            stmt = 'INSERT INTO '+ table_name1 + str(column_list) + ' SELECT '+ column_str +' FROM BM.'+table_name2 + ' where '+ condition
            #print stmt
            cur.execute(stmt)

        return 'done'



    def formulaToStrSubTable(self, formula):
        if not formula:
            return ''
        sList   = []
        for fDict in formula:
            for k, v in fDict.items():
                fDict[str(k)] = str(v)
            fStr    = fDict['POSITION'] + ':|:' + fDict['OPERATOR'] + ':|:' + fDict['GIVEN_VAL'] + ':|:' + fDict['CALC_VAL'] + ':|:' + fDict['PH_VAL'] + ':|:' + fDict['TAXO'] + ':|:' + fDict['TABLE_TYPE'] + ':|:' + fDict['LABEL'] + ':|:' + fDict['FORMULA_TYPE'] + ':|:' + str(fDict['ASSUMPTION_FLAG']) + ':|:' + str(fDict.get('XMLIDS', '')) + ':|:' + str(fDict.get('DOC_ID', '')) + ':|:' + str(fDict.get('TABLE_ID', '')) + ':|:' + fDict.get('SEQUENCE_KEY', '') + ':|:' + fDict.get('TABLE_HEADER', '') + ':|:' + fDict.get('GROUP_LABEL', '') + ':|:' + fDict.get('LINE_ITEM_TYPE', '')+':|:'+ str(fDict.get('PARENT_TABLE_TYPE', '')) +':|:'+ str(fDict.get('PARENT_TAXO', '')) +':|:'+ str(fDict.get('HFACTOR', 1)) +':|:'+ str(fDict.get('QFACTOR', 1)) +':|:'+ str(fDict.get('FYFACTOR', 1))
            sList.append(fStr)
        return ':$:'.join(sList)


    def strToFormulaSubTable(self, formula_str):
        if not formula_str:
            return []
        formula   = []
        for fStr in formula_str.split(':$:'):
            f_data_li = fStr.split(':|:')
            PARENT_TABLE_TYPE, PARENT_TAXO, HFACTOR, QFACTOR, FYFACTOR  ='', '', 1, 1, 1
            if len(f_data_li) == 17:
                POSITION, OPERATOR, GIVEN_VAL, CALC_VAL, PH_VAL, TAXO, TABLE_TYPE, LABEL, FORMULA_TYPE, ASSUMPTION_FLAG, XMLIDS, DOC_ID, TABLE_ID,SEQUENCE_KEY,TABLE_HEADER,GROUP_LABEL,LINE_ITEM_TYPE  = fStr.split(':|:')
            elif len(f_data_li) == 19:
                POSITION, OPERATOR, GIVEN_VAL, CALC_VAL, PH_VAL, TAXO, TABLE_TYPE, LABEL, FORMULA_TYPE, ASSUMPTION_FLAG, XMLIDS, DOC_ID, TABLE_ID,SEQUENCE_KEY,TABLE_HEADER,GROUP_LABEL,LINE_ITEM_TYPE, PARENT_TABLE_TYPE, PARENT_TAXO   = fStr.split(':|:')
            else:
                POSITION, OPERATOR, GIVEN_VAL, CALC_VAL, PH_VAL, TAXO, TABLE_TYPE, LABEL, FORMULA_TYPE, ASSUMPTION_FLAG, XMLIDS, DOC_ID, TABLE_ID,SEQUENCE_KEY,TABLE_HEADER,GROUP_LABEL,LINE_ITEM_TYPE, PARENT_TABLE_TYPE, PARENT_TAXO, HFACTOR, QFACTOR, FYFACTOR   = fStr.split(':|:')
            fDict   = {'POSITION':POSITION, 'OPERATOR':OPERATOR, 'GIVEN_VAL':GIVEN_VAL, 'CALC_VAL':CALC_VAL, 'PH_VAL':PH_VAL, 'TAXO':TAXO, 'TABLE_TYPE':TABLE_TYPE, 'LABEL':LABEL, 'FORMULA_TYPE':FORMULA_TYPE, 'ASSUMPTION_FLAG':ASSUMPTION_FLAG, 'XMLIDS':XMLIDS, 'DOC_ID':DOC_ID, 'TABLE_ID':TABLE_ID, 'SEQUENCE_KEY':SEQUENCE_KEY, 'TABLE_HEADER':TABLE_HEADER, 'GROUP_LABEL':GROUP_LABEL, 'LINE_ITEM_TYPE':LINE_ITEM_TYPE, 'PARENT_TABLE_TYPE':PARENT_TABLE_TYPE, 'PARENT_TAXO':PARENT_TAXO, 'HFACTOR':HFACTOR, 'QFACTOR':QFACTOR, 'FYFACTOR':FYFACTOR
                      }
            formula.append(fDict)
        return formula

    def formulaToStr(self, formula):
        if not formula:
            return ''
        sList   = []
        for fDict in formula:
            for k, v in fDict.items():
                fDict[str(k)] = str(v)

            fStr    = fDict['POSITION'] + ':|:' + fDict['OPERATOR'] +':|:'+ fDict['GIVEN_VAL'] +':|:'+ fDict['CALC_VAL'] +':|:'+ fDict['PH_VAL'] +':|:'+ fDict['TAXO'] +':|:'+ fDict['TABLE_TYPE'] +':|:'+ fDict['LABEL'] + ':|:' + fDict['FORMULA_TYPE'] +':|:'+ str(fDict['ASSUMPTION_FLAG']) +':|:'+ str(fDict.get('XMLIDS', '')) +':|:'+ str(fDict.get('DOC_ID', '')) +':|:'+ str(fDict.get('TABLE_ID', ''))
            sList.append(fStr)
        return ':$:'.join(sList)


    def strToFormula(self, formula_str):
        if not formula_str:
            return []
        formula   = []
        for fStr in formula_str.split(':$:'):
            f_data_li = fStr.split(':|:')
            XMLIDS, DOC_ID, TABLE_ID = '', '', ''
            if len(f_data_li) == 10:
                POSITION, OPERATOR, GIVEN_VAL, CALC_VAL, PH_VAL, TAXO, TABLE_TYPE, LABEL, FORMULA_TYPE, ASSUMPTION_FLAG   = fStr.split(':|:')
            elif len(f_data_li) == 13:
                POSITION, OPERATOR, GIVEN_VAL, CALC_VAL, PH_VAL, TAXO, TABLE_TYPE, LABEL, FORMULA_TYPE, ASSUMPTION_FLAG, XMLIDS, DOC_ID, TABLE_ID   = fStr.split(':|:')
            fDict   = {'POSITION':POSITION, 'OPERATOR':OPERATOR, 'GIVEN_VAL':GIVEN_VAL, 'CALC_VAL':CALC_VAL, 'PH_VAL':PH_VAL, 'TAXO':TAXO, 'TABLE_TYPE':TABLE_TYPE, 'LABEL':LABEL, 'FORMULA_TYPE':FORMULA_TYPE, 'ASSUMPTION_FLAG':ASSUMPTION_FLAG, 'XMLIDS':XMLIDS, 'DOC_ID':DOC_ID, 'TABLE_ID':TABLE_ID}
            formula.append(fDict)
        return formula

    def read_pragma_table_info(self, conn, cur, db_file, table_name):
        sql_query = "pragma table_info(%s)"%table_name
        cur.execute(sql_query)
        column_schema = cur.fetchall()
        column_schema = [str(r[1]) for r in column_schema[:]]
        return column_schema

if __name__ == '__main__':
   sObj = sqLiteApi()
