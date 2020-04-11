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

void importCheck()
{
    printf ("Library is imported !.");
}

void getTracking(double V, double R1, double R2, double R3, double R4, double C, int ModeSimulasi, double tMax, double inc)
{
    /* DEKLARASI VARIABEL */
    double Tau; //koefisien waktu
    double t;    // waktu
    double V1, V2, V3, V4, I1, I2, I3, I4, Ic; // output karakteristik rangkaian (SI)
    int i; // index

    /* ALGORITMA */

    // input mode simulasi
        // Mode OP (kapasitor open circuit)
    if (ModeSimulasi == 1)
    {

        // Perhitungan
        V1 = V;
        V2 = ((R3 + R4)/(R1 + R3 + R4))*V;
        V4 = V2;
        V3 = (R4/(R1 + R3 + R4))*V;
        I2 = 0;
        Ic = 0;
        I1 = V / (R1 + R3 + R4);
        I3 = I1;
        I4 = I1;

        // Open File External
        FILE* fp;
        fp = fopen("HasilTracking.txt", "w");
        printf("Mencetak ke File...\n");
        fprintf(fp,"HASIL SIMULASI OP\n");
        fprintf(fp,"V1 \tV2 \tV3 \tV4 \tI1 \tI2 \tI3 \tI4 \tIc\n");

        // Print value
        fprintf(fp, "%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f\n",
                    V1, V2, V3, V4, I1, I2, I3, I4, Ic);

        printf("Pencetakan selesai");
        // Close File External
        fclose(fp);

    } else if (ModeSimulasi == 2)
    {  // Mode Transiens

       // Hitung panjang alokasi memori
       int nElemen = (int)floor(tMax/inc);

        // Perhitungan
        Tau = (((R1 * (R3 + R4))/(R1 + R3 + R4)) + R2)*C;

        // Open File External
        FILE* fp;
        fp = fopen("HasilTracking.txt", "w");
        printf("Mencetak ke File...\n");
        fprintf(fp,"HASIL TRACKING BESARAN LISTIK\n");
        fprintf(fp,"time \tV1 \tV2 \tV3 \tV4 \tI1 \tI2 \tI3 \tI4 \tIc\n");

        // Tracking Loop
        for (i = 0; i < nElemen+1; i++)
        {
            // Calculate time
            t = i*inc;

            //Calculate value every point
            V4 = ((R3 + R4)/(R1 + R3 + R4))*V*(1 - (exp(-1*(t/Tau))));
            Ic = (C/Tau)*((R3 + R4)/(R1 + R3 + R4))*V*(exp(-1*(t/Tau)));
            V2 = (Ic*R2) + V4;
            I3 = V2/(R3 + R4);
            I4 = I3;
            V3 = I4*R4;
            I1 = Ic + I3;
            I2 = Ic;
            V1 = V;

            fprintf(fp, "%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f \t%.4f\n",
                    t, V1, V2, V3, V4, I1, I2, I3, I4, Ic);
        }

        printf("Pencetakan selesai");

        fclose(fp);

    } else
    {
        printf("INPUT SALAH !");
    }
}

int main (void)
{
    double V  = 1;
    double R1 = 1;
    double R2 = 1;
    double R3 = 1;
    double R4 = 1;
    double C  = 1;
    int ModeSimulasi = 2;
    double tMax = 1;
    double inc = 0.6;

    getTracking(V, R1, R2, R3, R4, C, ModeSimulasi, tMax, inc);

    return 0;
}
