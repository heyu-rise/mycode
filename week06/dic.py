def dic_test(name, id):
    print(name, id)


x = {'name': '1', 'id': 2}
a = ['1', '2']
dic_test('1', '2')
dic_test(**x)
dic_test(*a)
