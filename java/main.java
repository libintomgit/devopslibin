// package com.company;

import java.util.Scanner;

class TotalPercentage{
    public static void main(String[] args) {
        System.out.println("Hi Libin Tom Kk");
        System.out.println("Enter the score...");
        
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the score for CLAR : ");
        Integer clar = sc.nextInt();
        System.out.print("Enter the score for CPP : ");
        Integer cpp = sc.nextInt();
        System.out.print("Enter the score for DEVOPS : ");
        Integer devops = sc.nextInt();
        System.out.print("Enter the score for BLOCKCHAIN : ");
        Integer blockchain = sc.nextInt();
        System.out.print("Enter the TOTAL FULL SCORE FOR ALL THE MODULES : ");
        Integer totalModuleSocre = sc.nextInt();

        Integer totalScore = clar + cpp + devops + blockchain;

        System.out.println("You total score of all the modules: " + totalScore);
        float totalPerc = ((float) totalScore / totalModuleSocre * 100);
        System.out.print("You total percentage of all the modules: " + totalPerc + " %");



}

    
}