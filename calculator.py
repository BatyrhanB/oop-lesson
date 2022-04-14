class Calculator:
    '''Class for calculation methods'''
    def addition(*numbers): 
        result = 0
        for number in numbers:
            result += number
        return result
    
    def subtraction(*numbers):
        result = numbers[0]
        for number in numbers[1::]:
            result -= number
        return result

    def multiplication(*numbers):
        result = 1
        for number in numbers:
            result *= number
        return result

    def division(*numbers):
        result = numbers[0]
        for number in numbers[1::]:
            result /= number
        return result

