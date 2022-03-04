  .globl __start
  
  .data
msg1: .asciiz "mueva el disco de la torre: "
msg2: .asciiz " hacia la torre: "
msg3: .asciiz "\n"

  .text

  __start:
# llamando a hanoi(3, 1, 2, 3)
# 3 discos, torre origen = 1, torre destino = 2, torre alterna = 3
li a0 3
li a1 1
li a2 2
li a3 3
jal hanoi

# terminando el programa
li a0 10
ecall



# --------------------------------------
# Usted solo debe modificar esta funcion
# --------------------------------------
  hanoi:

# escriba
# su
# codigo
# aqui

# -------------------------------
# No modifique nada mas que hanoi
# -------------------------------



# recibe dos argumentos: origen y destino
  hanoiPrint:
addi sp sp -8
sw s0 0(sp)
sw s1 4(sp)
mv s0 a0
mv s1 a1
li a0 4
la a1 msg1
ecall
li a0 1
mv a1 s0
ecall
li a0 4
la a1 msg2
ecall
li a0 1
mv a1 s1
ecall
li a0 4
la a1 msg3
ecall
lw s0 0(sp)
lw s1 4(sp)
addi sp sp 8
jr ra
