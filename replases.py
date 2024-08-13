@app.route('/far_east/Amur_region/grafic_VRP')
def far_east_Amur_region_grafic_VRP():
    variable_to_pass_tupe = "VRP"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_Bezrabotica')
def far_east_Amur_region_grafic_Bezrabotica():
    variable_to_pass_tupe = "Bezrabotica"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_innovation')
def far_east_Amur_region_grafic_innovation():
    variable_to_pass_tupe = "innovation"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_iznos')
def far_east_Amur_region_grafic_iznos():
    variable_to_pass_tupe = "iznos"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_RabSila')
def far_east_Amur_region_grafic_RabSila():
    variable_to_pass_tupe = "RabSila"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_Trud')
def far_east_Amur_region_grafic_Trud():
    variable_to_pass_tupe = "Trud"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_ZP')
def far_east_Amur_region_grafic_ZP():
    variable_to_pass_tupe = "ZP"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')

@app.route('/far_east/Amur_region/grafic_VredProizv')
def far_east_Amur_region_grafic_VredProizv():
    variable_to_pass_tupe = "VredProizv"
    variable_to_pass_region = "Дальневосточный федеральный округ"
    variable_to_pass_link = "/far_east/Amur_region/"
    os.system(f'python3 grafic.py "{variable_to_pass_tupe}" "{variable_to_pass_region}" "{variable_to_pass_link}"')
    return render_template('grafic.html')


_VRP
_RabSila
_Trud
_VredProizv
_ZP
_Bezrabotica
_innovation
_iznos


<a href="/far_east/Amur_region/korrel_analiz">
<a href="/far_east/Amur_region/grafic_VRP">
<a href="/far_east/Amur_region/grafic_RabSila">
<a href="/far_east/Amur_region/grafic_Trud">
<a href="/far_east/Amur_region/grafic_VredProizv">
<a href="/far_east/Amur_region/regress_analiz">
<a href="/far_east/Amur_region/grafic_ZP">
<a href="/far_east/Amur_region/grafic_Bezrabotica">
<a href="/far_east/Amur_region/grafic_innovation">
<a href="/far_east/Amur_region/grafic_iznos">