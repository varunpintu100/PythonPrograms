package practice;

import java.util.HashSet;

public class LongestSubString {
	public static 	int longestSub(String s)
	{
		int i=0;
		int j=0;
		int max=0;
		HashSet<Character> set = new HashSet<>();
		while(j<s.length())
		{
			if(!set.contains(s.charAt(j)))
			{
				set.add(s.charAt(j));
				j++;
				max=Math.max(max, set.size());
			}
			else 
			{
				set.remove(s.charAt(i));
				i++;
			}
		}
		return max;
		
	}

	public static void main(String[] args) {
		
		System.out.println(longestSub("abcabcbb"));
		
		

	}

}
