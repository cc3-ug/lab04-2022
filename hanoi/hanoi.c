#include <stdio.h>

/* Forward declarations para evitarme los warnings */
void hanoi();
void hanoiPrint();


void main() {
    hanoi(3, 1, 2, 3);
}

/* Su tarea en este laboratorio es traducir esta funcion a RISC-V */
void hanoi(int numeroDeDiscos, int T_origen, int T_destino, int T_alterna) {
    if (numeroDeDiscos == 1) {
        hanoiPrint(T_origen, T_destino);
    } else {
        hanoi(numeroDeDiscos - 1, T_origen, T_alterna, T_destino);
        hanoi(1, T_origen, T_destino, T_alterna);
        hanoi(numeroDeDiscos - 1, T_alterna, T_destino, T_origen);
    }
}

/* Esta ya esta implementada en ensamblador */
void hanoiPrint(int T_origen, int T_destino) {
    printf("mueva el disco de la torre: ");
    printf("%i", T_origen);
    printf(" hacia la torre: ");
    printf("%i", T_destino);
    printf("\n");
}