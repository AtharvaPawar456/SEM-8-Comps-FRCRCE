import java.io.*;
import java.util.Scanner;

class Main {
    static int n;
    static int pro[] = new int[100];
    static int sta[] = new int[100];
    static int co;

    public static void main(String args[]) throws IOException {
        System.out.println("Enter the number of process");
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        int i, j, k, l, m;
        for (i = 0; i < n; i++) {
            System.out.println("For process " + (i + 1) + ":");
            System.out.println("Status:");
            sta[i] = in.nextInt();
            System.out.println("Priority");
            pro[i] = in.nextInt();
        }
        System.out.println("Which process will initiate the election?");
        int ele = in.nextInt();
        elect(ele);
        System.out.println("Final coordinator is " + co);
    }

static void elect(int ele) 
{ 
ele = ele-1; 
co = ele+1; 
for(int i=0;i<n;i++) 
{ 
if(pro[ele]<pro[i]) 
{ 
System.out.println("Election message is sent from "+(ele+1)+" to "+(i+1)); if(sta[i]==1) elect(i+1); 
} 
} 
}
}




PS C:\Users\Atharva Pawar\Documents\GitHub\SEM-8-Comps-FRCRCE\Distributed-Computing-DC\lab\exp - 7 - Election Algorithms> java Main
Enter the number of process
6
For process 1:
For process 4:
Status:
6
Priority
8
For process 5:
Status:
4
Priority
2
For process 6:
Status:
4
Priority
6
Which process will initiate the election?
4
Final coordinator is 4