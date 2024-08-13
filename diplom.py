from flask import Flask, render_template, request, jsonify, make_response
import os



app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Словарь, содержащий соответствие между названиями регионов и их URL
regions = {
    'Центральный': '/central',
    'Северо-Западный': '/northwest',
    'Южный' : '/south',
    'Приволжский': '/volga',
    'Уральский': '/ural',
    'Сибирский': '/siberia',
    'Дальневосточный': '/far_east',
    'Северо-Кавказский': '/north_caucasus',
}

# Обработчик маршрута для главной страницы
@app.route('/')
def index():
    return render_template('mainpage.html', regions=regions)

@app.route('/AnalizRF/')
def AnalizRF():
    return render_template('AnalizRF.html')

@app.route('/AnalizRF/regress_analiz')
def AnalizRF_regress_analiz():
    return render_template('reganaliz_AnalizRF.html')

@app.route('/AnalizRF/regres_analiz', methods=['POST'])
def AnalizRF_regres_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Российская Федерация"
    variable_to_pass_link = "/AnalizRF/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/AnalizRF/korrel_analiz')
def AnalizRF_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_AnalizRF.html')

@app.route('/AnalizRF/korrel_analiz', methods=['POST'])
def AnalizRF_korrel_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Российская Федерация"
    variable_to_pass_link = "/AnalizRF/"

    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')

    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response


@app.route('/AnalizRF/grafic_VRP')
def AnalizRF_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Российская Федерация"
    variable_to_pass_link = "/AnalizRF/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/AnalizRF/grafic_Bezrabotica')
def AnalizRF_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Российская Федерация"
    variable_to_pass_link = "/AnalizRF/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/AnalizRF/grafic_innovation')
def AnalizRF_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Российская Федерация"
    variable_to_pass_link = "/AnalizRF/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/AnalizRF/grafic_iznos')
def AnalizRF_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Российская Федерация"
    variable_to_pass_link = "/AnalizRF/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/AnalizRF/grafic_RabSila')
def AnalizRF_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Российская Федерация"
    variable_to_pass_link = "/AnalizRF/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/AnalizRF/grafic_Trud')
def AnalizRF_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Российская Федерация"
    variable_to_pass_link = "/AnalizRF/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/AnalizRF/grafic_ZP')
def AnalizRF_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Российская Федерация"
    variable_to_pass_link = "/AnalizRF/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/AnalizRF/grafic_VredProizv')
def AnalizRF_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Российская Федерация"
    variable_to_pass_link = "/AnalizRF/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

# Обработчик маршрута для страницы региона
@app.route('/far_east/')
def far_east():
    return render_template('far_east.html')

@app.route('/far_east/Amur_region/')
def far_east_Amur_region():
    return render_template('Amur_region.html')

@app.route('/far_east/Amur_region/regress_analiz')
def far_east_Amur_region_regress_analiz():
    return render_template('reganaliz_Amur_region.html')

@app.route('/Amur_region/regres_analiz', methods=['POST'])
def Amur_region_regres_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Амурская область"
    variable_to_pass_link = "/far_east/Amur_region/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/Amur_region/korrel_analiz')
def far_east_Amur_region_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_Amur_region.html')

@app.route('/Amur_region/korrel_analiz', methods=['POST'])
def Amur_region_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Амурская область"
    variable_to_pass_link = "/far_east/Amur_region/"

    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')

    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/Amur_region/grafic_VRP')
def far_east_Amur_region_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Амурская область"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_Bezrabotica')
def far_east_Amur_region_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Амурская область"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_innovation')
def far_east_Amur_region_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Амурская область"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_iznos')
def far_east_Amur_region_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Амурская область"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')

    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_RabSila')
def far_east_Amur_region_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Амурская область"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')

    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_Trud')
def far_east_Amur_region_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Амурская область"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')

    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_ZP')
def far_east_Amur_region_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Амурская область"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')

    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_VredProizv')
def far_east_Amur_region_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Амурская область"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')

    return render_template('grafic.html')

@app.route('/far_east/Analizfar_east/')
def far_east_Analizfar_east():
    return render_template('Analizfar_east.html')

@app.route('/far_east/Analizfar_east/regress_analiz')
def far_east_regress_analiz():
    return render_template('reganaliz_far_east.html')

@app.route('/far_east/regres_analiz', methods=['POST'])
def far_east_regres_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Российская Федерация"
    variable_to_pass_link = "/far_east"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/Analizfar_east/korrel_analiz')
def far_east_Analizfar_east_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_far_east.html')

@app.route('/Analizfar_east/korrel_analiz', methods=['POST'])
def korrel_analiz_Analizfar_east():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))

    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response    

@app.route('/far_east/Analizfar_east/grafic_VRP')
def far_east_Analizfar_east_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Analizfar_east/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Analizfar_east/grafic_Bezrabotica')
def far_east_Analizfar_east_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Analizfar_east/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Analizfar_east/grafic_innovation')
def far_east_Analizfar_east_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Analizfar_east/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Analizfar_east/grafic_iznos')
def far_east_Analizfar_east_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Analizfar_east/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Analizfar_east/grafic_RabSila')
def far_east_Analizfar_east_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Analizfar_east/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Analizfar_east/grafic_Trud')
def far_east_Analizfar_east_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Analizfar_east/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Analizfar_east/grafic_ZP')
def far_east_Analizfar_east_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Analizfar_east/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Analizfar_east/grafic_VredProizv')
def far_east_Analizfar_east_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Analizfar_east/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Chukotka_Autonomous_Okrug/')
def far_east_Chukotka_Autonomous_Okrug():
    return render_template('Chukotka_Autonomous_Okrug.html')


@app.route('/far_east/Chukotka_Autonomous_Okrug/regress_analiz')
def far_east_Chukotka_Autonomous_Okrug_regress_analiz():
    return render_template('reganaliz_Chukotka_Autonomous_Okrug.html')

@app.route('/Chukotka_Autonomous_Okrug/regres_analiz', methods=['POST'])
def far_east_Chukotka_Autonomous_Okrug_regres_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Чукотский автономный округ"
    variable_to_pass_link = "/far_east/Chukotka_Autonomous_Okrug/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/Chukotka_Autonomous_Okrug/korrel_analiz')
def far_east_Chukotka_Autonomous_Okrug_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_Chukotka_Autonomous_Okrug.html')

@app.route('/Chukotka_Autonomous_Okrug/korrel_analiz', methods=['POST'])
def far_east_Chukotka_Autonomous_Okrug_korrel_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Чукотский автономный округ"
    variable_to_pass_link = "/far_east/Chukotka_Autonomous_Okrug/"

    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')

    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response


@app.route('/far_east/Chukotka_Autonomous_Okrug/grafic_VRP')
def far_east_Chukotka_Autonomous_Okrug_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Чукотский автономный округ"
    variable_to_pass_link = "/far_east/Chukotka_Autonomous_Okrug/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Chukotka_Autonomous_Okrug/grafic_Bezrabotica')
def far_east_Chukotka_Autonomous_Okrug_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Чукотский автономный округ"
    variable_to_pass_link = "/far_east/Chukotka_Autonomous_Okrug/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Chukotka_Autonomous_Okrug/grafic_innovation')
def far_east_Chukotka_Autonomous_Okrug_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Чукотский автономный округ"
    variable_to_pass_link = "/far_east/Chukotka_Autonomous_Okrug/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Chukotka_Autonomous_Okrug/grafic_iznos')
def far_east_Chukotka_Autonomous_Okrug_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Чукотский автономный округ"
    variable_to_pass_link = "/far_east/Chukotka_Autonomous_Okrug/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Chukotka_Autonomous_Okrug/grafic_RabSila')
def far_east_Chukotka_Autonomous_Okrug_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Чукотский автономный округ"
    variable_to_pass_link = "/far_east/Chukotka_Autonomous_Okrug/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Chukotka_Autonomous_Okrug/grafic_Trud')
def far_east_Chukotka_Autonomous_Okrug_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Чукотский автономный округ"
    variable_to_pass_link = "/far_east/Chukotka_Autonomous_Okrug/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Chukotka_Autonomous_Okrug/grafic_ZP')
def far_east_Chukotka_Autonomous_Okrug_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Чукотский автономный округ"
    variable_to_pass_link = "/far_east/Chukotka_Autonomous_Okrug/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Chukotka_Autonomous_Okrug/grafic_VredProizv')
def far_east_Chukotka_Autonomous_Okrug_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Чукотский автономный округ"
    variable_to_pass_link = "/far_east/Chukotka_Autonomous_Okrug/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Kamchatka_Territory/')
def far_east_Kamchatka_Territory():
    return render_template('Kamchatka_Territory.html')


@app.route('/far_east/Kamchatka_Territory/regress_analiz')
def far_east_Kamchatka_Territory_regress_analiz():
    return render_template('reganaliz_Kamchatka_Territory.html')

@app.route('/Kamchatka_Territory/regres_analiz', methods=['POST'])
def far_east_Kamchatka_Territory_regres_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Камчатский край"
    variable_to_pass_link = "/far_east/Kamchatka_Territory/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/Kamchatka_Territory/korrel_analiz')
def far_east_Kamchatka_Territory_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_Kamchatka_Territory.html')

@app.route('/Kamchatka_Territory/korrel_analiz', methods=['POST'])
def far_east_Kamchatka_Territory_korrel_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Камчатский край"
    variable_to_pass_link = "/far_east/Kamchatka_Territory/"

    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')

    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response


@app.route('/far_east/Kamchatka_Territory/grafic_VRP')
def far_east_Kamchatka_Territory_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Камчатский край"
    variable_to_pass_link = "/far_east/Kamchatka_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Kamchatka_Territory/grafic_Bezrabotica')
def far_east_Kamchatka_Territory_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Камчатский край"
    variable_to_pass_link = "/far_east/Kamchatka_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Kamchatka_Territory/grafic_innovation')
def far_east_Kamchatka_Territory_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Камчатский край"
    variable_to_pass_link = "/far_east/Kamchatka_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Kamchatka_Territory/grafic_iznos')
def far_east_Kamchatka_Territory_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Камчатский край"
    variable_to_pass_link = "/far_east/Kamchatka_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Kamchatka_Territory/grafic_RabSila')
def far_east_Kamchatka_Territory_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Камчатский край"
    variable_to_pass_link = "/far_east/Kamchatka_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Kamchatka_Territory/grafic_Trud')
def far_east_Kamchatka_Territory_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Камчатский край"
    variable_to_pass_link = "/far_east/Kamchatka_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Kamchatka_Territory/grafic_ZP')
def far_east_Kamchatka_Territory_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Камчатский край"
    variable_to_pass_link = "/far_east/Kamchatka_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Kamchatka_Territory/grafic_VredProizv')
def far_east_Kamchatka_Territory_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Камчатский край"
    variable_to_pass_link = "/far_east/Kamchatka_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Khabarovsk_Territory/')
def far_east_Khabarovsk_Territory():
    return render_template('Khabarovsk_Territory.html')


@app.route('/far_east/Khabarovsk_Territory/regress_analiz')
def far_east_Khabarovsk_Territory_regress_analiz():
    return render_template('reganaliz_Khabarovsk_Territory.html')

@app.route('/Khabarovsk_Territory/regres_analiz', methods=['POST'])
def far_east_Khabarovsk_Territory_regres_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Хабаровский край"
    variable_to_pass_link = "/far_east/Khabarovsk_Territory/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/Khabarovsk_Territory/korrel_analiz')
def far_east_Khabarovsk_Territory_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_Khabarovsk_Territory.html')

@app.route('/Khabarovsk_Territory/korrel_analiz', methods=['POST'])
def far_east_Khabarovsk_Territory_korrel_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Хабаровский край"
    variable_to_pass_link = "/far_east/Khabarovsk_Territory/"

    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')

    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response


@app.route('/far_east/Khabarovsk_Territory/grafic_VRP')
def far_east_Khabarovsk_Territory_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Хабаровский край"
    variable_to_pass_link = "/far_east/Khabarovsk_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Khabarovsk_Territory/grafic_Bezrabotica')
def far_east_Khabarovsk_Territory_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Хабаровский край"
    variable_to_pass_link = "/far_east/Khabarovsk_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Khabarovsk_Territory/grafic_innovation')
def far_east_Khabarovsk_Territory_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Хабаровский край"
    variable_to_pass_link = "/far_east/Khabarovsk_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Khabarovsk_Territory/grafic_iznos')
def far_east_Khabarovsk_Territory_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Хабаровский край"
    variable_to_pass_link = "/far_east/Khabarovsk_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Khabarovsk_Territory/grafic_RabSila')
def far_east_Khabarovsk_Territory_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Хабаровский край"
    variable_to_pass_link = "/far_east/Khabarovsk_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Khabarovsk_Territory/grafic_Trud')
def far_east_Khabarovsk_Territory_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Хабаровский край"
    variable_to_pass_link = "/far_east/Khabarovsk_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Khabarovsk_Territory/grafic_ZP')
def far_east_Khabarovsk_Territory_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Хабаровский край"
    variable_to_pass_link = "/far_east/Khabarovsk_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Khabarovsk_Territory/grafic_VredProizv')
def far_east_Khabarovsk_Territory_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Хабаровский край"
    variable_to_pass_link = "/far_east/Khabarovsk_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Magadan_region/')
def far_east_Magadan_region():
    return render_template('Magadan_region.html')


@app.route('/far_east/Magadan_region/regress_analiz')
def far_east_Magadan_region_regress_analiz():
    return render_template('reganaliz_Magadan_region.html')

@app.route('/Magadan_region/regres_analiz', methods=['POST'])
def far_east_Magadan_region_regres_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Магаданская область"
    variable_to_pass_link = "/far_east/Magadan_region/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/Magadan_region/korrel_analiz')
def far_east_Magadan_region_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_Magadan_region.html')

@app.route('/Magadan_region/korrel_analiz', methods=['POST'])
def far_east_Magadan_region_korrel_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Магаданская область"
    variable_to_pass_link = "/far_east/Magadan_region/"

    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')

    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response




@app.route('/far_east/Magadan_region/grafic_VRP')
def far_east_Magadan_region_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Магаданская область"
    variable_to_pass_link = "/far_east/Magadan_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Magadan_region/grafic_Bezrabotica')
def far_east_Magadan_region_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Магаданская область"
    variable_to_pass_link = "/far_east/Magadan_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Magadan_region/grafic_innovation')
def far_east_Magadan_region_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Магаданская область"
    variable_to_pass_link = "/far_east/Magadan_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Magadan_region/grafic_iznos')
def far_east_Magadan_region_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Магаданская область"
    variable_to_pass_link = "/far_east/Magadan_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Magadan_region/grafic_RabSila')
def far_east_Magadan_region_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Магаданская область"
    variable_to_pass_link = "/far_east/Magadan_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Magadan_region/grafic_Trud')
def far_east_Magadan_region_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Магаданская область"
    variable_to_pass_link = "/far_east/Magadan_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Magadan_region/grafic_ZP')
def far_east_Magadan_region_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Магаданская область"
    variable_to_pass_link = "/far_east/Magadan_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Magadan_region/grafic_VredProizv')
def far_east_Magadan_region_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Магаданская область"
    variable_to_pass_link = "/far_east/Magadan_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Primorsky_Krai/')
def far_east_Primorsky_Krai():
    return render_template('Primorsky_Krai.html')

@app.route('/far_east/Primorsky_Krai/regress_analiz')
def far_east_Primorsky_Krai_regress_analiz():
    return render_template('reganaliz_Primorsky_Krai.html')

@app.route('/Primorsky_Krai/regres_analiz', methods=['POST'])
def far_east_Primorsky_Krai_regres_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Приморский край"
    variable_to_pass_link = "/far_east/Primorsky_Krai/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/Primorsky_Krai/korrel_analiz')
def far_east_Primorsky_Krai_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_Primorsky_Krai.html')

@app.route('/Primorsky_Krai/korrel_analiz', methods=['POST'])
def far_east_Primorsky_Krai_korrel_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Приморский край"
    variable_to_pass_link = "/far_east/Primorsky_Krai/"

    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')

    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response





@app.route('/far_east/Primorsky_Krai/grafic_VRP')
def far_east_Primorsky_Krai_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Приморский край"
    variable_to_pass_link = "/far_east/Primorsky_Krai/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Primorsky_Krai/grafic_Bezrabotica')
def far_east_Primorsky_Krai_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Приморский край"
    variable_to_pass_link = "/far_east/Primorsky_Krai/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Primorsky_Krai/grafic_innovation')
def far_east_Primorsky_Krai_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Приморский край"
    variable_to_pass_link = "/far_east/Primorsky_Krai/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Primorsky_Krai/grafic_iznos')
def far_east_Primorsky_Krai_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Приморский край"
    variable_to_pass_link = "/far_east/Primorsky_Krai/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Primorsky_Krai/grafic_RabSila')
def far_east_Primorsky_Krai_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Приморский край"
    variable_to_pass_link = "/far_east/Primorsky_Krai/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Primorsky_Krai/grafic_Trud')
def far_east_Primorsky_Krai_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Приморский край"
    variable_to_pass_link = "/far_east/Primorsky_Krai/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Primorsky_Krai/grafic_ZP')
def far_east_Primorsky_Krai_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Приморский край"
    variable_to_pass_link = "/far_east/Primorsky_Krai/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Primorsky_Krai/grafic_VredProizv')
def far_east_Primorsky_Krai_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Приморский край"
    variable_to_pass_link = "/far_east/Primorsky_Krai/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Buryatia/')
def far_east_Republic_of_Buryatia():
    return render_template('Republic_of_Buryatia.html')

@app.route('/far_east/Republic_of_Buryatia/regress_analiz')
def far_east_Republic_of_Buryatia_regress_analiz():
    return render_template('reganaliz_Republic_of_Buryatia.html')

@app.route('/Republic_of_Buryatia/regres_analiz', methods=['POST'])
def far_east_Republic_of_Buryatia_regres_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Республика Бурятия"
    variable_to_pass_link = "/far_east/Republic_of_Buryatia/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/Republic_of_Buryatia/korrel_analiz')
def far_east_Republic_of_Buryatia_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_Republic_of_Buryatia.html')

@app.route('/Republic_of_Buryatia/korrel_analiz', methods=['POST'])
def far_east_Republic_of_Buryatia_korrel_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Республика Бурятия"
    variable_to_pass_link = "/far_east/Republic_of_Buryatia/"

    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')

    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response




@app.route('/far_east/Republic_of_Buryatia/grafic_VRP')
def far_east_Republic_of_Buryatia_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Республика Бурятия"
    variable_to_pass_link = "/far_east/Republic_of_Buryatia/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Buryatia/grafic_Bezrabotica')
def far_east_Republic_of_Buryatia_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Республика Бурятия"
    variable_to_pass_link = "/far_east/Republic_of_Buryatia/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Buryatia/grafic_innovation')
def far_east_Republic_of_Buryatia_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Республика Бурятия"
    variable_to_pass_link = "/far_east/Republic_of_Buryatia/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Buryatia/grafic_iznos')
def far_east_Republic_of_Buryatia_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Республика Бурятия"
    variable_to_pass_link = "/far_east/Republic_of_Buryatia/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Buryatia/grafic_RabSila')
def far_east_Republic_of_Buryatia_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Республика Бурятия"
    variable_to_pass_link = "/far_east/Republic_of_Buryatia/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Buryatia/grafic_Trud')
def far_east_Republic_of_Buryatia_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Республика Бурятия"
    variable_to_pass_link = "/far_east/Republic_of_Buryatia/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Buryatia/grafic_ZP')
def far_east_Republic_of_Buryatia_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Республика Бурятия"
    variable_to_pass_link = "/far_east/Republic_of_Buryatia/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Buryatia/grafic_VredProizv')
def far_east_Republic_of_Buryatia_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Республика Бурятия"
    variable_to_pass_link = "/far_east/Republic_of_Buryatia/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Sakha/')
def far_east_Republic_of_Sakha():
    return render_template('Republic_of_Sakha.html')

@app.route('/far_east/Republic_of_Sakha/regress_analiz')
def far_east_Republic_of_Sakha_regress_analiz():
    return render_template('reganaliz_Republic_of_Sakha.html')

@app.route('/Republic_of_Sakha/regres_analiz', methods=['POST'])
def far_east_Republic_of_Sakha_regres_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Республика Саха (Якутия)"
    variable_to_pass_link = "/far_east/Republic_of_Sakha/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/Republic_of_Sakha/korrel_analiz')
def far_east_Republic_of_Sakha_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_Republic_of_Sakha.html')

@app.route('/Republic_of_Sakha/korrel_analiz', methods=['POST'])
def far_east_Republic_of_Sakha_korrel_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Республика Саха (Якутия)"
    variable_to_pass_link = "/far_east/Republic_of_Sakha/"

    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')

    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response



@app.route('/far_east/Republic_of_Sakha/grafic_VRP')
def far_east_Republic_of_Sakha_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Республика Саха (Якутия)"
    variable_to_pass_link = "/far_east/Republic_of_Sakha/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Sakha/grafic_Bezrabotica')
def far_east_Republic_of_Sakha_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Республика Саха (Якутия)"
    variable_to_pass_link = "/far_east/Republic_of_Sakha/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Sakha/grafic_innovation')
def far_east_Republic_of_Sakha_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Республика Саха (Якутия)"
    variable_to_pass_link = "/far_east/Republic_of_Sakha/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Sakha/grafic_iznos')
def far_east_Republic_of_Sakha_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Республика Саха (Якутия)"
    variable_to_pass_link = "/far_east/Republic_of_Sakha/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Sakha/grafic_RabSila')
def far_east_Republic_of_Sakha_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Республика Саха (Якутия)"
    variable_to_pass_link = "/far_east/Republic_of_Sakha/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Sakha/grafic_Trud')
def far_east_Republic_of_Sakha_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Республика Саха (Якутия)"
    variable_to_pass_link = "/far_east/Republic_of_Sakha/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Sakha/grafic_ZP')
def far_east_Republic_of_Sakha_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Республика Саха (Якутия)"
    variable_to_pass_link = "/far_east/Republic_of_Sakha/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Republic_of_Sakha/grafic_VredProizv')
def far_east_Republic_of_Sakha_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Республика Саха (Якутия)"
    variable_to_pass_link = "/far_east/Republic_of_Sakha/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Sakhalin_region/')
def far_east_Sakhalin_region():
    return render_template('Sakhalin_region.html')

@app.route('/far_east/Sakhalin_region/regress_analiz')
def far_east_Sakhalin_region_regress_analiz():
    return render_template('reganaliz_Sakhalin_region.html')

@app.route('/Sakhalin_region/regres_analiz', methods=['POST'])
def far_east_Sakhalin_region_regres_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Сахалинская область"
    variable_to_pass_link = "/far_east/Sakhalin_region/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/Sakhalin_region/korrel_analiz')
def far_east_Sakhalin_region_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_Sakhalin_region.html')

@app.route('/Sakhalin_region/korrel_analiz', methods=['POST'])
def far_east_Sakhalin_region_korrel_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Сахалинская область"
    variable_to_pass_link = "/far_east/Sakhalin_region/"

    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')

    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response


@app.route('/far_east/Sakhalin_region/grafic_VRP')
def far_east_Sakhalin_region_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Сахалинская область"
    variable_to_pass_link = "/far_east/Sakhalin_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Sakhalin_region/grafic_Bezrabotica')
def far_east_Sakhalin_region_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Сахалинская область"
    variable_to_pass_link = "/far_east/Sakhalin_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Sakhalin_region/grafic_innovation')
def far_east_Sakhalin_region_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Сахалинская область"
    variable_to_pass_link = "/far_east/Sakhalin_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Sakhalin_region/grafic_iznos')
def far_east_Sakhalin_region_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Сахалинская область"
    variable_to_pass_link = "/far_east/Sakhalin_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Sakhalin_region/grafic_RabSila')
def far_east_Sakhalin_region_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Сахалинская область"
    variable_to_pass_link = "/far_east/Sakhalin_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Sakhalin_region/grafic_Trud')
def far_east_Sakhalin_region_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Сахалинская область"
    variable_to_pass_link = "/far_east/Sakhalin_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Sakhalin_region/grafic_ZP')
def far_east_Sakhalin_region_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Сахалинская область"
    variable_to_pass_link = "/far_east/Sakhalin_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Sakhalin_region/grafic_VredProizv')
def far_east_Sakhalin_region_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Сахалинская область"
    variable_to_pass_link = "/far_east/Sakhalin_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/The_Jewish_Autonomous_Region/')
def far_east_The_Jewish_Autonomous_Region():
    return render_template('The_Jewish_Autonomous_Region.html')

@app.route('/far_east/The_Jewish_Autonomous_Region/regress_analiz')
def far_east_The_Jewish_Autonomous_Region_regress_analiz():
    return render_template('reganaliz_The_Jewish_Autonomous_Region.html')

@app.route('/The_Jewish_Autonomous_Region/regres_analiz', methods=['POST'])
def far_east_The_Jewish_Autonomous_Region_regres_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Еврейская автономная область"
    variable_to_pass_link = "/far_east/The_Jewish_Autonomous_Region/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/The_Jewish_Autonomous_Region/korrel_analiz')
def far_east_The_Jewish_Autonomous_Region_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_The_Jewish_Autonomous_Region.html')

@app.route('/The_Jewish_Autonomous_Region/korrel_analiz', methods=['POST'])
def far_east_The_Jewish_Autonomous_Region_korrel_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Еврейская автономная область"
    variable_to_pass_link = "/far_east/The_Jewish_Autonomous_Region/"

    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')

    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response



@app.route('/far_east/The_Jewish_Autonomous_Region/grafic_VRP')
def far_east_The_Jewish_Autonomous_Region_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Еврейская автономная область"
    variable_to_pass_link = "/far_east/The_Jewish_Autonomous_Region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/The_Jewish_Autonomous_Region/grafic_Bezrabotica')
def far_east_The_Jewish_Autonomous_Region_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Еврейская автономная область"
    variable_to_pass_link = "/far_east/The_Jewish_Autonomous_Region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/The_Jewish_Autonomous_Region/grafic_innovation')
def far_east_The_Jewish_Autonomous_Region_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Еврейская автономная область"
    variable_to_pass_link = "/far_east/The_Jewish_Autonomous_Region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/The_Jewish_Autonomous_Region/grafic_iznos')
def far_east_The_Jewish_Autonomous_Region_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Еврейская автономная область"
    variable_to_pass_link = "/far_east/The_Jewish_Autonomous_Region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/The_Jewish_Autonomous_Region/grafic_RabSila')
def far_east_The_Jewish_Autonomous_Region_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Еврейская автономная область"
    variable_to_pass_link = "/far_east/The_Jewish_Autonomous_Region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/The_Jewish_Autonomous_Region/grafic_Trud')
def far_east_The_Jewish_Autonomous_Region_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Еврейская автономная область"
    variable_to_pass_link = "/far_east/The_Jewish_Autonomous_Region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/The_Jewish_Autonomous_Region/grafic_ZP')
def far_east_The_Jewish_Autonomous_Region_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Еврейская автономная область"
    variable_to_pass_link = "/far_east/The_Jewish_Autonomous_Region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/The_Jewish_Autonomous_Region/grafic_VredProizv')
def far_east_The_Jewish_Autonomous_Region_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Еврейская автономная область"
    variable_to_pass_link = "/far_east/The_Jewish_Autonomous_Region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Trans-Baikal_Territory/')
def far_east_Trans_Baikal_Territory():
    return render_template('Trans-Baikal_Territory.html')

@app.route('/far_east/Trans-Baikal_Territory/regress_analiz')
def far_east_Trans_Baikal_Territory_regress_analiz():
    return render_template('reganaliz_Trans-Baikal_Territory.html')

@app.route('/Trans-Baikal_Territory/regres_analiz', methods=['POST'])
def far_east_Trans_Baikal_Territory_regres_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Забайкальский край"
    variable_to_pass_link = "/far_east/Trans-Baikal_Territory/"
    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')
    import regres_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = regres_analiz.html_img
    corr_2 = regres_analiz.reg_ur
    R2 = regres_analiz.r_squared

    response = make_response(jsonify(corr_2=corr_2, R2=R2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response

@app.route('/far_east/Trans-Baikal_Territory/korrel_analiz')
def far_east_Trans_Baikal_Territory_korrel_analiz():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    return render_template('koranaliz_Trans-Baikal_Territory.html')

@app.route('/Trans-Baikal_Territory/korrel_analiz', methods=['POST'])
def far_east_Trans_Baikal_Territory_korrel_analiz_post():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    data = request.get_json()
    print(data)
    variable_to_pass_type_1 = data['variable1']
    variable_to_pass_type_2 = data['variable2']
    variable_to_pass_region = "Забайкальский край"
    variable_to_pass_link = "/far_east/Trans-Baikal_Territory/"

    with open('data.txt', 'w') as f:
        f.write(f'{variable_to_pass_type_1}\n{variable_to_pass_type_2}\n{variable_to_pass_region}\n{variable_to_pass_link}')

    import korrel_analiz
    pngImageB64String = ''
    corr_2 = 0
    pngImageB64String = korrel_analiz.pngImageB64String
    corr_2 = korrel_analiz.corr_2

    response = make_response(jsonify(corr_2=corr_2, pngImageB64String=pngImageB64String))
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response




@app.route('/far_east/Trans-Baikal_Territory/grafic_VRP')
def far_east_Trans_Baikal_Territory_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Забайкальский край"
    variable_to_pass_link = "/far_east/Trans-Baikal_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Trans-Baikal_Territory/grafic_Bezrabotica')
def far_east_Trans_Baikal_Territory_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Забайкальский край"
    variable_to_pass_link = "/far_east/Trans-Baikal_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Trans-Baikal_Territory/grafic_innovation')
def far_east_Trans_Baikal_Territory_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Забайкальский край"
    variable_to_pass_link = "/far_east/Trans-Baikal_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Trans-Baikal_Territory/grafic_iznos')
def far_east_Trans_Baikal_Territory_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Забайкальский край"
    variable_to_pass_link = "/far_east/Trans-Baikal_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Trans-Baikal_Territory/grafic_RabSila')
def far_east_Trans_Baikal_Territory_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Забайкальский край"
    variable_to_pass_link = "/far_east/Trans-Baikal_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Trans-Baikal_Territory/grafic_Trud')
def far_east_Trans_Baikal_Territory_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Забайкальский край"
    variable_to_pass_link = "/far_east/Trans-Baikal_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Trans-Baikal_Territory/grafic_ZP')
def far_east_Trans_Baikal_Territory_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Забайкальский край"
    variable_to_pass_link = "/far_east/Trans-Baikal_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Trans-Baikal_Territory/grafic_VredProizv')
def far_east_Trans_Baikal_Territory_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Забайкальский край"
    variable_to_pass_link = "/far_east/Trans-Baikal_Territory/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/central/')
def central():
    return render_template('central.html')

@app.route('/south/')
def south():
    return render_template('south.html')

@app.route('/northwest/')
def northwest():
    return render_template('northwest.html')

@app.route('/privolg/')
def volga():
    return render_template('privolg.html')

@app.route('/ural/')
def ural():
    return render_template('ural.html')

@app.route('/siberia/')
def siberia():
    return render_template('siberia.html')

@app.route('/north_caucasus/')
def north_caucasus():
    return render_template('north_caucasus.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
