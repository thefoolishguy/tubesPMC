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

    // FUNGSI DAN PROCEDURE
    // Fungsi Tau
    double getTau (double V, double R1, double R2, double R3, double R4, double C)
    {
        double Tau = (((R1 * (R3 + R4))/(R1 + R3 + R4)) + R2)*C;
        return Tau;
    }

    // Procedure V1
    void getV1 (double V, double R1, double R2, double R3, double R4, double C, int ModeSimulasi, double tMax, double inc)
    {
        // Algoritma
            // OP
        if (ModeSimulasi == 1)
        {
            // Library Local
            double V1;

             // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            V1 = V;

            // Print to file
            fprintf(fp,"HASIL SIMULASI OP\n");
            fprintf(fp,"V1\n");
            fprintf(fp, "%.4lf", V1);

            // Close File
            fclose(fp);

        } else if ( ModeSimulasi == 2)
        { // TRANS

            // Library Local
            double V1;
            double t;
            double Tau;
            int i;

            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            Tau = getTau(V, R1, R2, R3, R4, C);

            // Hitung panjang alokasi memori
            int nElemen = ((int)(tMax/inc)+1);

            // Print to file
            fprintf(fp,"HASIL SIMULASI TRANS\n");
            fprintf(fp,"time \tV1\n");

            // Tracking Loop
            for (i = 0; i < nElemen+1; i++)
            {
                // Calculate time
                t = i*inc;

                //Calculate value every point
                V1 = V;

                fprintf(fp, "%.4lf \t%.4lf", t, V1);
            }

            // Close File
            fclose(fp);

        } else
        {
            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            fprintf(fp, "SALAH INPUT !");

            fclose(fp);
        }
    }

    // Procedure V2
    void getV2 (double V, double R1, double R2, double R3, double R4, double C, int ModeSimulasi, double tMax, double inc)
    {
        // Algoritma
            // OP
        if (ModeSimulasi == 1)
        {
            // Library Local
            double V2;

             // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            V2 = ((R3 + R4)/(R1 + R3 + R4))*V;

            // Print to file
            fprintf(fp,"HASIL SIMULASI OP\n");
            fprintf(fp,"V2\n");
            fprintf(fp, "%.4lf", V2);

            // Close File
            fclose(fp);

        } else if ( ModeSimulasi == 2)
        { // TRANS

            // Library Local
            double V4;
            double Ic;
            double V2;
            double t;
            double Tau;
            int i;

            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            Tau = getTau(V, R1, R2, R3, R4, C);

            // Hitung panjang alokasi memori
            int nElemen = ((int)(tMax/inc)+1);

            // Print to file
            fprintf(fp,"HASIL SIMULASI TRANS\n");
            fprintf(fp,"time \tV2\n");

            // Tracking Loop
            for (i = 0; i < nElemen+1; i++)
            {
                // Calculate time
                t = i*inc;

                //Calculate value every point
                V4 = ((R3 + R4)/(R1 + R3 + R4))*V*(1 - (exp(-1*(t/Tau))));
                Ic = (C/Tau)*((R3 + R4)/(R1 + R3 + R4))*V*(exp(-1*(t/Tau)));
                V2 = (Ic*R2) + V4;

                fprintf(fp, "%.4lf \t%.4lf", t, V2);
            }

            // Close File
            fclose(fp);

        } else
        {
            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            fprintf(fp, "SALAH INPUT !");

            fclose(fp);
        }
    }

    // Procedure V3
    void getV3 (double V, double R1, double R2, double R3, double R4, double C, int ModeSimulasi, double tMax, double inc)
    {
        // Algoritma
            // OP
        if (ModeSimulasi == 1)
        {
            // Library Local
            double V3;

             // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            V3 = (R4/(R1 + R3 + R4))*V;

            // Print to file
            fprintf(fp,"HASIL SIMULASI OP\n");
            fprintf(fp,"V3\n");
            fprintf(fp, "%.4lf", V3);

            // Close File
            fclose(fp);

        } else if ( ModeSimulasi == 2)
        { // TRANS

            // Library Local
            double V4;
            double V3;
            double I3;
            double Ic;
            double V2;
            double t;
            double Tau;
            int i;

            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            Tau = getTau(V, R1, R2, R3, R4, C);

            // Hitung panjang alokasi memori
            int nElemen = ((int)(tMax/inc)+1);

            // Print to file
            fprintf(fp,"HASIL SIMULASI TRANS\n");
            fprintf(fp,"time \tV2\n");

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
                V3 = I3*R4;

                fprintf(fp, "%.4lf \t%.4lf", t, V3);
            }

            // Close File
            fclose(fp);

        } else
        {
            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            fprintf(fp, "SALAH INPUT !");

            fclose(fp);
        }
    }

    // Procedure V4
    void getV4 (double V, double R1, double R2, double R3, double R4, double C, int ModeSimulasi, double tMax, double inc)
    {
        // Algoritma
            // OP
        if (ModeSimulasi == 1)
        {
            // Library Local
            double V4;

             // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            V4 = ((R3 + R4)/(R1 + R3 + R4))*V;

            // Print to file
            fprintf(fp,"HASIL SIMULASI OP\n");
            fprintf(fp,"V4\n");
            fprintf(fp, "%.4lf", V4);

            // Close File
            fclose(fp);

        } else if ( ModeSimulasi == 2)
        { // TRANS

            // Library Local
            double V4;
            double t;
            double Tau;
            int i;

            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            Tau = getTau(V, R1, R2, R3, R4, C);

            // Hitung panjang alokasi memori
            int nElemen = ((int)(tMax/inc)+1);

            // Print to file
            fprintf(fp,"HASIL SIMULASI TRANS\n");
            fprintf(fp,"time \tV2\n");

            // Tracking Loop
            for (i = 0; i < nElemen+1; i++)
            {
                // Calculate time
                t = i*inc;

                //Calculate value every point
                V4 = ((R3 + R4)/(R1 + R3 + R4))*V*(1 - (exp(-1*(t/Tau))));

                fprintf(fp, "%.4lf \t%.4lf", t, V4);
            }

            // Close File
            fclose(fp);

        } else
        {
            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            fprintf(fp, "SALAH INPUT !");

            fclose(fp);
        }
    }

    // Procedure I1
    void getI1 (double V, double R1, double R2, double R3, double R4, double C, int ModeSimulasi, double tMax, double inc)
    {
        // Algoritma
            // OP
        if (ModeSimulasi == 1)
        {
            // Library Local
            double I1;

             // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            I1 = V / (R1 + R3 + R4);

            // Print to file
            fprintf(fp,"HASIL SIMULASI OP\n");
            fprintf(fp,"I1\n");
            fprintf(fp, "%.4lf", I1);

            // Close File
            fclose(fp);

        } else if ( ModeSimulasi == 2)
        { // TRANS

            // Library Local
            double Ic;
            double V2;
            double I3;
            double I1;
            double V4;
            double t;
            double Tau;
            int i;

            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            Tau = getTau(V, R1, R2, R3, R4, C);

            // Hitung panjang alokasi memori
            int nElemen = ((int)(tMax/inc)+1);

            // Print to file
            fprintf(fp,"HASIL SIMULASI TRANS\n");
            fprintf(fp,"time \tI1\n");

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
                I1 = Ic + I3;

                fprintf(fp, "%.4lf \t%.4lf", t, I1);
            }

            // Close File
            fclose(fp);

        } else
        {
            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            fprintf(fp, "SALAH INPUT !");

            fclose(fp);
        }
    }

    // Procedure I2
    void getI2 (double V, double R1, double R2, double R3, double R4, double C, int ModeSimulasi, double tMax, double inc)
    {
        // Algoritma
            // OP
        if (ModeSimulasi == 1)
        {
            // Library Local
            double I2;

             // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            I2 = 0;

            // Print to file
            fprintf(fp,"HASIL SIMULASI OP\n");
            fprintf(fp,"I2\n");
            fprintf(fp, "%.4lf", I2);

            // Close File
            fclose(fp);

        } else if ( ModeSimulasi == 2)
        { // TRANS

            // Library Local
            double I2;
            double t;
            double Tau;
            int i;

            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            Tau = getTau(V, R1, R2, R3, R4, C);

            // Hitung panjang alokasi memori
            int nElemen = ((int)(tMax/inc)+1);

            // Print to file
            fprintf(fp,"HASIL SIMULASI TRANS\n");
            fprintf(fp,"time \tI2\n");

            // Tracking Loop
            for (i = 0; i < nElemen+1; i++)
            {
                // Calculate time
                t = i*inc;

                //Calculate value every point
                I2 = (C/Tau)*((R3 + R4)/(R1 + R3 + R4))*V*(exp(-1*(t/Tau)));

                fprintf(fp, "%.4lf \t%.4lf", t, I2);
            }

            // Close File
            fclose(fp);

        } else
        {
            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            fprintf(fp, "SALAH INPUT !");

            fclose(fp);
        }
    }

    // Procedure I3
    void getI3 (double V, double R1, double R2, double R3, double R4, double C, int ModeSimulasi, double tMax, double inc)
    {
        // Algoritma
            // OP
        if (ModeSimulasi == 1)
        {
            // Library Local
            double I3;

             // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            I3 = V / (R1 + R3 + R4);

            // Print to file
            fprintf(fp,"HASIL SIMULASI OP\n");
            fprintf(fp,"I3\n");
            fprintf(fp, "%.4lf", I3);

            // Close File
            fclose(fp);

        } else if ( ModeSimulasi == 2)
        { // TRANS

            // Library Local
            double V4;
            double Ic;
            double V2;
            double I3;
            double t;
            double Tau;
            int i;

            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            Tau = getTau(V, R1, R2, R3, R4, C);

            // Hitung panjang alokasi memori
            int nElemen = ((int)(tMax/inc)+1);

            // Print to file
            fprintf(fp,"HASIL SIMULASI TRANS\n");
            fprintf(fp,"time \tI3\n");

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

                fprintf(fp, "%.4lf \t%.4lf", t, I3);
            }

            // Close File
            fclose(fp);

        } else
        {
            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            fprintf(fp, "SALAH INPUT !");

            fclose(fp);
        }
    }

    // Procedure I4
    void getI4 (double V, double R1, double R2, double R3, double R4, double C, int ModeSimulasi, double tMax, double inc)
    {
        // Algoritma
            // OP
        if (ModeSimulasi == 1)
        {
            // Library Local
            double I4;

             // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            I4 = V / (R1 + R3 + R4);

            // Print to file
            fprintf(fp,"HASIL SIMULASI OP\n");
            fprintf(fp,"I4\n");
            fprintf(fp, "%.4lf", I4);

            // Close File
            fclose(fp);

        } else if ( ModeSimulasi == 2)
        { // TRANS

            // Library Local
            double V4;
            double Ic;
            double V2;
            double I4;
            double t;
            double Tau;
            int i;

            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            Tau = getTau(V, R1, R2, R3, R4, C);

            // Hitung panjang alokasi memori
            int nElemen = ((int)(tMax/inc)+1);

            // Print to file
            fprintf(fp,"HASIL SIMULASI TRANS\n");
            fprintf(fp,"time \tI3\n");

            // Tracking Loop
            for (i = 0; i < nElemen+1; i++)
            {
                // Calculate time
                t = i*inc;

                //Calculate value every point
                V4 = ((R3 + R4)/(R1 + R3 + R4))*V*(1 - (exp(-1*(t/Tau))));
                Ic = (C/Tau)*((R3 + R4)/(R1 + R3 + R4))*V*(exp(-1*(t/Tau)));
                V2 = (Ic*R2) + V4;
                I4 = V2/(R3 + R4);

                fprintf(fp, "%.4lf \t%.4lf", t, I4);
            }

            // Close File
            fclose(fp);

        } else
        {
            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            fprintf(fp, "SALAH INPUT !");

            fclose(fp);
        }
    }

    // Procedure Ic
    void getIc (double V, double R1, double R2, double R3, double R4, double C, int ModeSimulasi, double tMax, double inc)
    {
        // Algoritma
            // OP
        if (ModeSimulasi == 1)
        {
            // Library Local
            double Ic;

             // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            Ic = 0;

            // Print to file
            fprintf(fp,"HASIL SIMULASI OP\n");
            fprintf(fp,"I4\n");
            fprintf(fp, "%.4lf", Ic);

            // Close File
            fclose(fp);

        } else if ( ModeSimulasi == 2)
        { // TRANS

            // Library Local
            double Ic;
            double t;
            double Tau;
            int i;

            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            // Perhitungan
            Tau = getTau(V, R1, R2, R3, R4, C);

            // Hitung panjang alokasi memori
            int nElemen = ((int)(tMax/inc)+1);

            // Print to file
            fprintf(fp,"HASIL SIMULASI TRANS\n");
            fprintf(fp,"time \tI3\n");

            // Tracking Loop
            for (i = 0; i < nElemen+1; i++)
            {
                // Calculate time
                t = i*inc;

                //Calculate value every point
                Ic = (C/Tau)*((R3 + R4)/(R1 + R3 + R4))*V*(exp(-1*(t/Tau)));

                fprintf(fp, "%.4lf \t%.4lf", t, Ic);
            }

            // Close File
            fclose(fp);

        } else
        {
            // Open File External
            FILE* fp;
            fp = fopen("HasilTracking.txt", "w");

            fprintf(fp, "SALAH INPUT !");

            fclose(fp);
        }
    }

    // PROGRAM UTAMA
int main (void)
{
    /* DEKLARASI VARIABEL */
    double V, R1, R2, R3, R4, C; // input nilai komponen (SI)
    double Tau; //koefisien waktu
    double tMax;   // Waktu Maksimum
    double inc; // increment waktu
    // double *t, *V2, *V3, *V4, *V5, *I1, *I2, *I3, *I4, *Ic;  output karakteristik rangkaian (SI)
    int ModeSimulasi; // ( 0 = OP/ 1 = TRANS)

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

}
