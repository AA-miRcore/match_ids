#################

match_ids documentation

author:	Nolan Kuza (nkuza8@gmail.com)
date:	11-15-18

#################

usage: match_ids.py [-h] file_A file_B output_file

Matches the TCGA ids listed in file A with those in file B and outputs the results to a file.

positional arguments:
  file_A       The name of the file containing the subset of TCGA ids to match
               with file B.
  file_B       The name of the larger file containing the TCGA ids and
               ascociated file names (tab seperated).
  output_file  The name of the file to output the results. If the file exists,
               it will be OVERWRITTEN.

optional arguments:
  -h, --help   show a help message and exit

examples:
	* To match TCGA ids in fileA.txt with those in fileB.txt, then output to out_file.txt:
		$ python match_ids.py fileA.txt fileB.txt out_file.txt

		fileA.txt
			TCGA-AA-0000
			TCGA-AA-0000
			TCGA-AA-0001
			TCGA-BB-0000
			
		fileB.txt
			TCGA-AA-0000    file1.vcf
			TCGA-AA-0001    file2.vcf
			TCGA-AA-0002    file3.vcf
			TCGA-BB-0000    file4.vcf
			TCGA-BB-0000    file5.vcf
			TCGA-BB-0001    file6.vcf
			TCGA-BB-0002    file7.vcf
			
		out_file.txt (after the program has ran)
			TCGA-AA-0000    file1.vcf
			TCGA-AA-0000    file1.vcf  
			TCGA-AA-0001    file2.vcf
			TCGA-BB-0000    file4.vcf
			TCGA-BB-0000    file5.vcf  

other:
	The output file will be created if it does not already exist.