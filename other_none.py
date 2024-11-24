primitive = [1, 22.0, True, False, [], (5,), {}, None]
def create_welcome_message(header: str  = '', users: list[str] = None) -> str | None:
    """
    create HTM H1 header according to https://threatmap.fortiguard.com/
    """
    if users is None:
        users = []
    users.append(header)
    if header:
        return f'<h1>{header}</h1>'
    return

def process_unpacked_data(args):
    print(args)
    print(*args)
    pass


iterable_sec = 1, 2, 3, 'ghghgh'
first, second, third, forth = iterable_sec
process_unpacked_data(iterable_sec)

result = create_welcome_message('', users=[])
result1 = create_welcome_message('555', ['hjhjhj'])
result2 = create_welcome_message()
pass
