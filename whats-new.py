exs = ExceptionGroup('Custom Exception message',
                     [FileNotFoundError('File A.png does not exist'),
                      FileNotFoundError('File B.png does not exist'),
                      KeyError('Key not found'),
                      ExceptionGroup('Nested Exception message', [
                          FileNotFoundError('File C.png does not exist'),
                          FileNotFoundError('File D.png does not exist'),
                          KeyError('Key not found')])
                      ])

try:
    raise exs
# except* FileNotFoundError as eg:
#     print(eg.exceptions)
# except* KeyError as eg:
#     print(eg.exceptions)
# except ExceptionGroup as eg:
#     print(eg.exceptions)
except* Exception as eg:
    for exc in eg.exceptions:
        if isinstance(exc, ExceptionGroup):
            try:
                raise exc
            except* Exception as e:
                print(f"\v{e.exceptions.__getitem__(0)}\v{e.exceptions.__getitem__(1)}\v{e.exceptions.__getitem__(2)}")
        else:
            print(exc)
