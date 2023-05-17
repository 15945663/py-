def add_numbers(num1, num2):
    return num1 + num2

numbers = []
while True:
    try:
        user_input = input("请输入一个数字，或输入 'done' 结束：")
        if user_input == 'done':
            break
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("无效的输入，请输入一个数字或 'done'。")

if len(numbers) < 2:
    print("至少需要输入两个数字。")
else:
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = add_numbers(result, numbers[i])
    print(f"{' + '.join(map(str, numbers))} = {result}")