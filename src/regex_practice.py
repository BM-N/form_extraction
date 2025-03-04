import re
re.IGNORECASE

def format_text(text):

    patterns = {
        "Idade": r'Idade\s*:\s*[^\n]+',
        "Prontuário": r'(Prontuário)\s*:\s*([^\n]+)',
        "Matrícula": r'(Matrícula)\s*:\s*([^\n]+)',
        "Nasc.": r'(Nasc\.)\s*([0-9/:_-]+)',
        "Data": r'(Data)\s*:\s*([0-9/:_-]+)',
        "Hora": r'(Hora)\s*:\s*([0-9:_-]+)',
        'DATA DA CIRURGIA': r'(DATA DA CIRURGIA)\s*:\s*([\s*0-9/:_-]+)',
        'HORÁRIO': r'(HORÁRIO)\s*:\s*([\n*0-9:]+)',
        'ESPECIALIDADE': r'(ESPECIALIDADE)\s*:\s*([a-zA-ZÀ-ÿ]+)',
        'CÓDIGO TUSS': r'(CÓDIGO TUSS)\s*:\s*([0-9]+)'
    }

    extracted_data = {}
            
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL)
        if match:
            extracted_data[key] = match.group().strip()

    def clean_multiline_data(data):
        return data.replace('_', '').replace('\n', '').replace(' /', '').strip('/')

    for key, value in extracted_data.items():
        extracted_data[key] = clean_multiline_data(extracted_data[key])
        
    final_dict = {}

    for key, value in extracted_data.items():
        if ':' in value:
            value1, value2 = value.split(sep=':', maxsplit=1)
            value1 = value1.strip()
            value2 = value2.strip()
        else:
            n = re.search(r'[A-Za-zÀ-ÿ]+', value)
            n = n.span()[1]
            value = value[:n] + ':' + value[n + 1:]
            value1, value2 = value.split(sep=':', maxsplit=1)
            value1 = value1.strip()
            value2 = value2.strip()
        # formatação para hora
        if value1.lower() in ['hora', 'horário']:
            hora = re.compile(r'^\d{2}:\d{2}$')
            if not bool(hora.match(value2)):
                if len(value2) == 4:
                    value2 = value2[:2] + ':' + value2[2:]
                else:
                    print(f"Value passed is not in horário format.")
        # Falta formatação para data
        if value1.lower() in ['data', 'Nasc', 'data da cirurgia']:
            data = re.compile(r'^\d{2}/\d{2}/\d{4}$')
            if not bool(data.match(value2)):
                if len(value2) == 6:
                    value2 = value2[:2] + '/' + value2[2:4] + '/20' + value2[4:]
                if len (value2)== 8: 
                    value2 = value2[:2] + '/' + value2[2:4] + '/' + value2[4:]
                if len(value2) == 7:
                    if value2.find('/') == 2:
                        value2=value2[:4] + "/" + value2[4:]
                    if value2.find('/') == 4:
                        value2=value2[:2] + "/" + value2[2:]
                    else:
                        print('Formatação inválida para a data')           

    # Maybe add data validation for each field. ex. number of digits, type of string etc.
        final_dict[value1.lower()] = value2.lower()
    
    return final_dict