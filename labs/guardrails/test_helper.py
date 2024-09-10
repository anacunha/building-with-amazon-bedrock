import sys, configparser

def get_guardrail_id(guardrail_example_type):
    try:
        config = configparser.ConfigParser()
        config.read('bwab_guardrails.ini')
        guardrail_id = config['guardrails'][guardrail_example_type]
    except:
        raise KeyError("Please run the appropriate create guardrail script indicated in the lab instructions.")

    return guardrail_id

def get_prompt_from_command_line():
    return sys.argv[1]

def set_guardrail_id(guardrail_example_type, guardrail_id):
    config = configparser.ConfigParser()
    config.read('bwab_guardrails.ini')
    
    if "guardrails" not in config:
        config['guardrails'] = {}
    
    config['guardrails'][guardrail_example_type] = guardrail_id
    
    with open('bwab_guardrails.ini', 'w') as configfile:
        config.write(configfile)