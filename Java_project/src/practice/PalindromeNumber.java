package practice;

public class PalindromeNumber {
	public static boolean PalinNumber(int n)
	{
		if(n<0 || n!=0&&n%10==0)
			return false;
		int temp=0;
		while(n>temp)
		{
			temp = temp*10+n%10;
			n=n/10;
		}
		return(n==temp||n==temp/10);
	}
	public static void main(String[] args)
	{
		System.out.println(PalinNumber(-121));
	}

}
