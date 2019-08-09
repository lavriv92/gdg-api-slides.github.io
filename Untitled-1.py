import jsonschema

def validate(schema):
    v = jsonschema.Draft7Validator(schema)
    
    @wrapps(fn)
    def wrapper(fn):
        def wrapped(*args, **kwargs):
            errors = [e.message for e in v.iter_errors(request.json)]
            
            if errors:
                return reply_json({ 'errors': errors })
            
            return fn(*args, *kwargs)
        return wrapped
    return wrapper