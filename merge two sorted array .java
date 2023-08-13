public class Main
{
	public static void main(String[] args) {
		int []a = {1,2,3};
		int []b = {2,4,5};
		merge(a,b);
	}
	public static void merge(int a[],int b[]){
	    int i=0,j=0;
	    while(i<a.length && j<b.length){
	        if(a[i]<=b[j]){
	            System.out.print(a[i]+" ");
	            i++;
	        }
	        else{
	            System.out.print(b[j]+" ");
	            j++;
	        }
	    }
	    while(i<a.length){
	        System.out.print(a[i]);
	        i++;
	    }
	    while(j<b.length){
	        System.out.print(b[j]+" ");
	        j++;
	    }
	}
}
