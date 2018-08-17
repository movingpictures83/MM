import sys
#import numpy
import PyPluMA


class MMPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      firstline = filestuff.readline()
      self.bacteria = firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = []
      i = 0
      for line in filestuff:
         contents = line.split(',')
	 self.ADJ.append([])
         for j in range(self.n):
            value = float(contents[j+1])
            if (i != j and value != 0):
               self.ADJ[i].append(value)
            else:
               self.ADJ[i].append(0)
         i += 1

   def output(self, filename):
      #gmlfilename = self.myfile[0:len(self.myfile)-3] + "gml"
      #gmlfile = open(gmlfilename, 'w')
      noafile = open(filename, 'w')
      PyPluMA.log("Writing NOA file ")

      noafile.write("name\tMM\n")
      for bac in self.bacteria:
         bac = bac.strip()
         if (bac[0] == '\"'):
            bac = bac[1:len(bac)-1]
         if (bac[0] == 'X'):
            noafile.write(bac+"\t1\n")
         else:
            noafile.write(bac+"\t0\n")




