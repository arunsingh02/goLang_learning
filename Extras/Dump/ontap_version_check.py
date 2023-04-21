from pdb import set_trace

def test():
    #set_trace()
    ontap_version = 'Lighthouse__9.13.0'
    digit = suffix = ''
    img_ver_val = ontap_version.split('.')[:2]
    
    if len(img_ver_val) > 1:
        for index, char in enumerate(img_ver_val[1]):
            if char.isdigit():
                digit = digit + char
            else:
                suffix = img_ver_val[1][index:]
                break

        digit = "{0:02d}".format(int(digit))

        img_ver_val[1] = digit + suffix
        img_ver_val = '.'.join(i for i in img_ver_val)
    else:
        img_ver_val = '.'.join(i for i in img_ver_val)

    # get rid of any prefix R or suffix -*console as it does not affect sorting
    img_ver_val = (
        img_ver_val.replace('R9', '9').replace('-vidconsole', '')
        .replace('-serialconsole', '')
    )

    # if this is a GA image, it will be of the form 9.6 without any suffixes
    if len(img_ver_val) == 4:
        img_ver_val += '2'

    # do our replacements as described above
    img_ver_val = (
        img_ver_val.replace('xN', '4').replace('RC', '1').replace('P', '5')
        .replace('devN', '999').replace('dev', '999').replace('_', '.').replace('R', '').replace('X', '3').replace('Lighthouse', '')
    )

    # for consistency's sake, pad out each segment with 0s to make them all
    # the same length. Fixes issues trying to assert 9.5P1 < 9.6 (9.531 vs 9.62)
    while len(img_ver_val.split('.')) < 4:
        img_ver_val += '.0'
    img_ver_val = '.'.join([segment.ljust(6, '0') for segment in img_ver_val.split('.')])

    # return an integer which wraps all the above
    print(img_ver_val.replace('.', ''))
    return int(img_ver_val.replace('.', ''))

test()
