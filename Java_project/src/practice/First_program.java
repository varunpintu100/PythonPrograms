package practice;

import java.util.Arrays;

//import java.util.Scanner;

public class First_program {  // mycode
	public static int[] parity(int[] arr)
	{
		int temp=0;
		for(int i=0;i<arr.length/2;i++)
		{
			for(int j=0;j<arr.length/2;j++)
			{
			if(arr[(2*i)+1]%2==0)
			{ 
				if(arr[2*j]%2!=0)
				{
					temp=arr[2*j];
					arr[2*j]=arr[(2*i)+1];
					arr[(2*i)+1]=temp;
				}
				}
			}
			}
		return arr;
        
	}
	public static int[] parity1(int[] arr)
	{ // the better code version
		int temp=0,even=0,odd=1;
		while(even<arr.length && odd<arr.length)
		{
			if(arr[even]%2!=0)
			{
				System.out.println(arr[even]);
				temp=arr[even];
				System.out.println("The value of temp changes to : "+arr[even]);
				arr[even]=arr[odd];
				System.out.println("The value at even place changes to :"+arr[odd]);
				arr[odd]=temp;
				System.out.println("The value of odd place changes to :"+temp);
				odd+=2;
			}
			else
				even+=2;
		}
		return arr;
	}
	public static void main(String[] args) {
	//Scanner input = new Scanner(System.in); this is used to take input
	int[] arr= {1,2,4,6,8,10,3,5,7,9};
	System.out.println(Arrays.toString(parity1(arr)));
	System.out.println(Arrays.toString(parity(arr)));
}
}