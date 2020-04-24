from aip import AipOcr
APP_ID = '18010790'
API_KEY = 'c9uo1Z9H5VzxufTxqCjyKYZG'
SECRET_KEY = 'FgDnCKZU2ayv4iZHy8RCp98HlPtCK3Mn'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

def baidu_ocr(path):
    image = get_file_content(path)
    client.basicGeneral(image)
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"
    res = client.basicGeneral(image, options)
    res_str = res['words_result']
    res_str_all = ''
    for i in range(len(res_str)):
        res_str_a = res['words_result'][i]['words']
        res_str_all += res_str_a
    return res_str_all
