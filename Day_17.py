# pylint: disable=trailing-whitespace, missing-module-docstring, missing-function-docstring, missing-class-docstring, missing-final-newline, invalid-name, trailing-newlines, wrong-import-position, unused-import
import pygame
import kittehs_funkollection as kf

inp = "input"
registers, program = kf.eat(inp, "")

A = kf.find_ints(registers[0])[0]
B = kf.find_ints(registers[1])[0]
C = kf.find_ints(registers[2])[0]
program = kf.find_ints(program[0])

print(A, B, C)
print(program)

def get_operand_value(op, A, B, C):
    if op <= 3:
        return op
    if op == 4:
        return A
    if op == 5:
        return B
    if op == 6:
        return C
    return None

def run_program(program, A, B, C):
    output = []
    pcounter = 0

    while pcounter < len(program):
        instruction = program[pcounter]
        pcounter += 1
        match (instruction):
            case 0:
                operand = program[pcounter]
                opvalue = get_operand_value(operand, A, B, C)
                A = A // (2 ** opvalue)
                pcounter += 1
            case 1:
                operand = program[pcounter]
                opvalue = operand
                B = B ^ opvalue
                pcounter += 1
            case 2:
                operand = program[pcounter]
                opvalue = get_operand_value(operand, A, B, C)
                B = opvalue % 8
                pcounter += 1
            case 3:
                operand = program[pcounter]
                opvalue = operand
                if A == 0:
                    #pass
                    pcounter += 1
                else:
                    pcounter = opvalue
            case 4:
                operand = program[pcounter]
                opvalue = get_operand_value(operand, A, B, C)
                B = B ^ C
                pcounter += 1
            case 5:
                operand = program[pcounter]
                opvalue = get_operand_value(operand, A, B, C)
                output.append(opvalue % 8)
                pcounter += 1
            case 6:
                operand = program[pcounter]
                opvalue = get_operand_value(operand, A, B, C)
                B = A // (2 ** opvalue)
                pcounter += 1
            case 7:
                operand = program[pcounter]
                opvalue = get_operand_value(operand, A, B, C)
                C = A // (2 ** opvalue)
                pcounter += 1
            case _:
                print(f"Unknown opcode {instruction}")
                break
    return output

output = run_program(program, A, B, C)
print(f"P1: {output}")

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Day 17')

A = 1
mult = 1
dirn = 1
last_matches = 0
for iterations in range(100000000):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_DOWN:
                dirn = -1
            elif event.key == pygame.K_UP:
                dirn = 1
            elif event.key == pygame.K_LEFT:
                mult = int(mult / 10)
                if mult == 0:
                    mult = 1
            elif event.key == pygame.K_RIGHT:
                mult = int(mult * 10)

    output = run_program(program, A, B, C)

    if output == program:
        print(f"P2: {A}")
        break

    if len(output) > len(program):
        print("Output too long")
    if len(output) < len(program):
        print("Output too short")

    good_ending = True
    matches = 0
    for i in range(12):
        if output[len(output) - i - 1] != program[len(program) - i - 1]:
            matches = i
            break
    if matches > last_matches and len(output) == 16:
        if dirn == 1:
            A -= mult
        else:
            A +=  mult
        mult = 1
    last_matches = matches

    print(A, matches, output, len(output), len(program), mult, dirn)
        
    if dirn == 1:
        A += mult
    else:
        A -= mult

