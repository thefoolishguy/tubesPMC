/* PROGRAM UNTUK MELAKUKAN SIMULASI RANGKAIAN */

/* Bentuk rangkaian sebagai berikut
            R1   V2    R3    V3
       V5|-===---|-----===----|
         |      | |           |
         |      | | R2       | |
        _|_      |         R4| |
      V  -       |V4          |
         |    C ===           |
         |-------|------------|
                 |
                gnd
*/

#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

int main (void)
{
    /* DEKLARASI VARIABEL */
    double V, R1, R2, R3, R4, C; // input nilai komponen (SI)
    double Tau; //koefisien waktu
    double *t, tMax;   // waktu
    double inc; // increment waktu
    double *V2, *V3, *V4, *V5, *I1, *I2, *I3, *I4, *Ic; // output karakteristik rangkaian (SI)
    char ModeSimulasi[6]; // (OP/TRANS)
    int i; // index

    /* ALGORITMA */
    // input besaran
    printf("PROGRAM SIMULASI RANGKAIAN\n");
    printf("Masukan input :\n");
    printf("V = ");
    scanf("%lf", &V);
    printf("R1 = ");
    scanf("%lf", &R1);
    printf("R2 = ");
    scanf("%lf", &R2);
    printf("R3 = ");
    scanf("%lf", &R3);
    printf("R4 = ");
    scanf("%lf", &R4);
    printf("C = ");
    scanf("%lf", &C);

    // input mode simulasi
    printf("\n");
    printf("Masukan mode simulasi (OP/TRANS) : ");
    scanf(" %s", ModeSimulasi);
        // Mode OP (kapasitor open circuit)
    if (!strcmp(ModeSimulasi, "OP"))
    {
        // Alokasi memori
        V2 = (double*)malloc(sizeof(double));
        V3 = (double*)malloc(sizeof(double));
        V4 = (double*)malloc(sizeof(double));
        V5 = (double*)malloc(sizeof(double));
        I1 = (double*)malloc(sizeof(double));
        I2 = (double*)malloc(sizeof(double));
        I3 = (double*)malloc(sizeof(double));
        I4 = (double*)malloc(sizeof(double));
        Ic = (double*)malloc(sizeof(double));

        // Perhitungan
        *V5 = V;
        *V2 = ((R3 + R4)/(R1 + R3 + R4))*V;
        *V4 = *V2;
        *V3 = (R4/(R1 + R3 + R4))*V;
        *I2 = 0;
        *Ic = 0;
        *I1 = V / (R1 + R3 + R4);
        *I3 = *I1;
        *I4 = *I1;

        // Cetak Besaran
        printf("\nHasil Simulasi OP diperoleh : \n");
        printf("V2 = %.4f Volt\n", *V2);
        printf("V3 = %.4f Volt\n", *V3);
        printf("V4 = %.4f Volt\n", *V4);
        printf("V5 = %.4f Volt\n", *V5);

        printf("I1 = %.4f Amp\n", *I1);
        printf("I2 = %.4f Amp\n", *I2);
        printf("I3 = %.4f Amp\n", *I3);
        printf("I4 = %.4f Amp\n", *I4);
        printf("Ic = %.4f Amp\n", *Ic);

    } else if (!strcmp(ModeSimulasi,"TRANS"))
    {  // Mode Transiens

       // Input parameter waktu
       printf("Masukan parameter waktu : \n");
       printf("t Max      (s) = ");
       scanf("%lf", &tMax);
       printf("t increment(s) = ");
       scanf("%lf", &inc);

       // Hitung panjang alokasi memori
       int nElemen = ((int)(tMax/inc)+1);

       // Inisiasi Alokasi memory
        t  = (double*)malloc(nElemen*sizeof(double));
        V2 = (double*)malloc(nElemen*sizeof(double));
        V3 = (double*)malloc(nElemen*sizeof(double));
        V4 = (double*)malloc(nElemen*sizeof(double));
        V5 = (double*)malloc(nElemen*sizeof(double));
        I1 = (double*)malloc(nElemen*sizeof(double));
        I2 = (double*)malloc(nElemen*sizeof(double));
        I3 = (double*)malloc(nElemen*sizeof(double));
        I4 = (double*)malloc(nElemen*sizeof(double));
        Ic = (double*)malloc(nElemen*sizeof(double));

        // Perhitungan
        Tau = (((R1 * (R3 + R4))/(R1 + R3 + R4)) + R2)*C;

        // Tracking Loop
        for (i = 0; i < nElemen+1; i++)
        {
            // Calculate time
            t[i] = i*inc;

            //Calculate value every point
            V4[i] = ((R3 + R4)/(R1 + R3 + R4))*V*(1 - (exp(-1*(t[i]/Tau))));
            Ic[i] = (C/Tau)*((R3 + R4)/(R1 + R3 + R4))*V*(exp(-1*(t[i]/Tau)));
            V2[i] = (Ic[i]*R2) + V4[i];
            I3[i] = V2[i]/(R3 + R4);
            I4[i] = I3[i];
            V3[i] = I4[i]*R4;
            I1[i] = Ic[i] + I3[i];
            I2[i] = Ic[i];
            V5[i] = V;

        }


        // Mencetak ke dan File

        // Open File External
        FILE* fp;
        fp = fopen("HasilTracking.txt", "w");
        printf("\nMencetak ke File...\n");
        fprintf(fp,"HASIL TRACKING BESARAN LISTIK\n");
        fprintf(fp,"time \tV2 \tV3 \tV4 \tV5 \tI1 \tI2 \tI3 \tI4 \tIc\n");

        for(i = 0; i < nElemen+1; i++)
        {
            fprintf(fp, "%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f\n",
                    t[i], V2[i], V3[i], V4[i], V5[i], I1[i], I2[i], I3[i], I4[i], Ic[i]);

        }
        printf("Pencetakan selesai");

        fclose(fp);
    }

    // Hapus Memori
        free(V2);
        free(V3);
        free(V4);
        free(V5);
        free(I1);
        free(I2);
        free(I3);
        free(I4);
        free(Ic);

    return 0;
}
