#include<stdio.h>
#include<string.h>
#include<sys/types.h>
#include<dirent.h>
   #include < linux/kernel.h >
    #include < linux/sched.h >
    #include < linux/module.h >
int main()
{

DIR *dp;
for_each_

struct dirent *ep;

dp=opendir("./homework/Assignment34");
if(dp!=NULL)
{
	while(ep=readdir(dp))
	{
		if(ep->d_type == DT_REG)
		{
	 		printf("%ld\t%s\n",ep->d_ino,ep->d_name);
		}
	}
	(void) closedir(dp);
}
else
{
	printf("Could not open the directory!\n");
}

/*char ch[]="Marvellous Infosystem.";

/*printf("Enter a character:");
scanf("%c",&ch);
int *ptr;
int a=10;
char * c= ch;
char ab[40];
char *q=ab;
ptr=&a;
while(*c)
{
*q++=*c++;
}
printf("Value in c:%c\n",*c);
printf("Value in q:%c\n",*q);
printf("Value in ab:%s\n",ab);
(*ptr)++;
printf("Value in ptr:%d\n",*ptr);*/

return 0;
}
