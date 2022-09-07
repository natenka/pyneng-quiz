all_questions = {
    "04 Строки": [
        {
            "description": "Какое значение будет у переменной result в последней строке?",
            "code": "string = 'interface'\nresult = string[3]",
            "answers": {
                "1": "'t'",
                "2": "'inte'",
                "3": "'int'",
                "4": "'e'",
                "5": "'r'",
                "6": "Ошибка",
            },
            "correct_answer": "4",
            "multiple_choices": False,
        },
        {
            "description": "Какое значение будет у переменной result в последней строке?",
            "code": "string = 'interface'\nresult = string[:4]",
            "answers": {
                "1": "'t'",
                "2": "'int'",
                "3": "'e'",
                "4": "'r'",
                "5": "'inte'",
                "6": "Ошибка",
            },
            "correct_answer": "5",
            "multiple_choices": False,
        },
        {
            "description": "Какое значение будет у переменной result в последней строке?",
            "code": "string = 'interface'\nresult = string[:]",
            "answers": {
                "1": "''",
                "2": "'interface'",
                "3": "Ошибка",
            },
            "correct_answer": "2",
            "multiple_choices": False,
        },
        {
            "description": "Какое значение будет у переменной result в последней строке?",
            "code": "string = 'interface'\nresult = string[::2]",
            "answers": {
                "1": "Ошибка",
                "2": "''",
                "3": "'interface'",
                "4": "'itrae'",
                "5": "'nefc'",
                "6": "'in'",
            },
            "correct_answer": "4",
            "multiple_choices": False,
        },
    ],
    "04 Строки и списки": [
        {
            "description": "Какое значение будет у переменной result в последней строке?",
            "code": "string = 'FastEthernet0/1    10.1.1.1  255.255.255.0'\nresult = string.split()[-2]",
            "answers": {
                "1": "Ошибка",
                "2": "''",
                "3": "'255.255.255.0'",
                "4": "'10.1.1.1'",
                "5": "'FastEthernet0/1'",
            },
            "correct_answer": "4",
            "multiple_choices": False,
        },
        {
            "description": "Какое значение будет у переменной result в последней строке?",
            "code": "string = 'FastEthernet0/1    10.1.1.1  255.255.255.0'\nresult = string.split()[-1].split('.')",
            "answers": {
                "1": "Ошибка",
                "2": "''",
                "3": "['255', '255', '255', '0']",
                "4": "['10', '1', '1', '1']",
                "5": "['FastEthernet0/1']",
                "6": "[255, 255, 255, 0]",
                "7": "[10, 1, 1, 1]",
            },
            "correct_answer": "3",
            "multiple_choices": False,
        },
        {
            "description": "Какое значение будет у переменной result в последней строке?",
            "code": "string = 'FastEthernet0/1    10.1.1.1  255.255.255.0'\nresult = string.split().split('.')",
            "answers": {
                "1": "Ошибка",
                "2": "''",
                "3": "['255', '255', '255', '0']",
                "4": "['10', '1', '1', '1']",
                "5": "['FastEthernet0/1']",
                "6": "['FastEthernet0/1    10', '1', '1', '1  255', '255', '255', '0']",
            },
            "correct_answer": "1",
            "multiple_choices": False,
        },
    ],
    "04 Словари": [
        {
            "description": "Какое значение будет у переменной result в последней строке?",
            "code": "result = {}\nresult[1] = 100\nresult[1] = 200",
            "answers": {
                "1": "Ошибка",
                "2": "''",
                "3": "['255', '255', '255', '0']",
                "4": "['10', '1', '1', '1']",
                "5": "['FastEthernet0/1']",
                "6": "['FastEthernet0/1    10', '1', '1', '1  255', '255', '255', '0']",
            },
            "correct_answer": "1",
            "multiple_choices": False,
        },
    ],
    "04 Типы данных и функции преобразования типов": [
        {
            "description": "Какое значение будет у переменной result в последней строке?",
            "code": "item = '101'\nresult = int(item, 2)",
            "answers": {
                "1": "101",
                "2": "7",
                "3": "4",
                "4": "5",
                "5": "'101'",
                "6": "Ошибка",
            },
            "correct_answer": "4",
            "multiple_choices": False,
        },
        {
            "description": "Какое значение id будет у переменной var_b?",
            "code": "In [1]: var_a = var_b = 3500\n\nIn [2]: id(var_a)\nOut[2]: 3044598608",
            "answers": {
                "1": "3044598608",
                "2": "Другое",
            },
            "correct_answer": "1",
            "multiple_choices": False,
        },
        {
            "description": "Какое значение будет у переменной result в последней строке?",
            "code": "item = '101'\nresult = int(item, 10)",
            "answers": {
                "1": "101",
                "2": "7",
                "3": "4",
                "4": "5",
                "5": "'101'",
                "6": "Ошибка",
            },
            "correct_answer": "1",
            "multiple_choices": False,
        },
        {
            "description": "Какое значение id будет у переменной var_b?",
            "code": "In [1]: var_a = 3500\n\nIn [2]: var_b = 3500\n\nIn [3]: id(var_a)\nOut[3]: 3044599696",
            "answers": {
                "1": "3044599696",
                "2": "Другое",
            },
            "correct_answer": "2",
            "multiple_choices": False,
        },
        {
            "description": "Какое значение будет у переменной result в последней строке?",
            "code": "number = 10\nresult = hex(number)",
            "answers": {
                "1": "10",
                "2": "'a'",
                "3": "'0xa'",
                "4": "'0x10'",
                "5": "Ошибка",
            },
            "correct_answer": "3",
            "multiple_choices": False,
        },
        {
            "description": "Какое значение будет у переменной number в последней строке?",
            "code": "number = 10\nnumber += 2",
            "answers": {
                "1": "2",
                "2": "12",
                "3": "10",
                "4": "Ошибка",
            },
            "correct_answer": "2",
            "multiple_choices": False,
        },
    ],
}

