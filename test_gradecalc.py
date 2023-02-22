import unittest
import rawcode_gradecalc
from rawcode_gradecalc import calc_final_worth
from rawcode_gradecalc import grade_wanted
from rawcode_gradecalc import grade_after_final

class Test_rawgradecalc(unittest.TestCase): 

    def test_calc_final_worth(self):

      # Normal Boundary Value Tests 
      
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.calc_final_worth(500,0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(500,1000),50.0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(500,1),50000.0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(500,999),50.05)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(0,500),0.0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(1000,500),200.0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(1,500),0.2)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(999,500),199.8)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(500,500),100.0)
      
      
      # Robust Boundary Value Tests 
      
      with self.assertRaises(ValueError):
          rawcode_gradecalc.calc_final_worth(-1,500)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(1001,500),200.2)
      with self.assertRaises(ValueError):
          rawcode_gradecalc.calc_final_worth(500,-1)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(500,1001),49.95)    


      # Worst Case Boundary Value Tests 
      
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.calc_final_worth(0,0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(0,1),0.0)   
      self.assertEqual(rawcode_gradecalc.calc_final_worth(0,1000),0.0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(0,999),0.0)
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.calc_final_worth(1,0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(1,1),100.0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(1,1000),0.1)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(1,999),0.1)
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.calc_final_worth(1000,0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(1000,1),100000.0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(1000,1000),100.0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(1000,999),100.1)
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.calc_final_worth(999,0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(999,1),99900.0)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(999,1000),99.9)
      self.assertEqual(rawcode_gradecalc.calc_final_worth(999,999),100.0)


     # Path & Coverage Testing 
     # line 1

      with self.assertRaises(ValueError): 
          rawcode_gradecalc.calc_final_worth("&&","*")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.calc_final_worth("&",100)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.calc_final_worth(100,"!!")
      self.assertEqual(rawcode_gradecalc.calc_final_worth(30,600),5.0)
      
      # line 2
      
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.calc_final_worth("a","z")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.calc_final_worth("c", 200)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.calc_final_worth("!","!!!")
      self.assertEqual(rawcode_gradecalc.calc_final_worth(90,1200),7.5)
      
      # line 3 
      
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.calc_final_worth("AB","Z")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.calc_final_worth("Ty","!")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.calc_final_worth("#","B")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.calc_final_worth("#","#")
      
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.calc_final_worth("","")
          
     
   
    def test_grade_wanted(self): 
        
        # Normal Boundary Value Tests 
        
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(50,0,50)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,50,50),50.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,50,50),-50.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,50,50),150.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,50,50),-48.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,50,50),148.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,100,50),50.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,1,50),50.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,99,50),50.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,50,0),100.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,50,100),0.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,50,1),99.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,50,99),1.0)
      
      
      # Robust Boundary Value Tests 
      
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted(-1,50,50)
      self.assertEqual(rawcode_gradecalc.grade_wanted(101,50,50),152.0)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted(50,-1,50)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,101,50),50.0)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted(50,50,-1)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,50,101),-1.0)
      
      
      # Worst Case Boundary Value Tests 
      
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(0,0,0)
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(1,0,0)
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(50,0,0)
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(99,0,0)  
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(100,0,0)
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(0,0,1)
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(1,0,1)
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(50,0,1)
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(99,0,1)
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(100,0,1) 
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(0,0,50)   
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(1,0,50)    
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(99,0,50) 
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(100,0,50)  
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(0,0,99)  
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(1,0,99)    
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(50,0,99) 
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(99,0,99) 
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(100,0,99) 
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(0,0,100) 
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(1,0,100) 
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(50,0,100) 
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(99,0,100) 
      with self.assertRaises(ZeroDivisionError): 
          rawcode_gradecalc.grade_wanted(100,0,100) 
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,1,0),0.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,1,0),100.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,1,0),5000.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,1,0),9900.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,1,0),10000.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,1,1),-99.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,1,1),1.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,1,1),4901.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,1,1),9801.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,1,1),9901.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,1,50),-4950.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,1,50),-4850.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,1,50),4950.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,1,50),5050.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,1,99),-9801.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,1,99),-9701.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,1,99),-4801.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,1,99),99.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,1,99),199.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,1,100),-9900.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,1,100),-9800.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,1,100),-4900.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,1,100),0.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,1,100),100.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,50,0),0.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,50,0),2.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,50,0),198.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,50,0),200.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,50,1),-1.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,50,1),1.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,50,1),197.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,50,1),199.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,50,99),-99.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,50,99),-97.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,50,99),99.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,50,99),101.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,50,100),-100.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,50,100),-98.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,50,100),98.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,50,100),100.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,99,0),0.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,99,0),1.01)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,99,0),50.51)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,99,0),100.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,99,0),101.01)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,99,1),-0.01)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,99,1),1.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,99,1),50.49)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,99,1),99.99)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,99,1),101.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,99,50),-0.51)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,99,50),0.51)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,99,50),99.49)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,99,50),100.51)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,99,99),-1.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,99,99),0.01)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,99,99),49.51)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,99,99),99.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,99,99),100.01)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,99,100),-1.01)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,99,100),0.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,99,100),49.49)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,99,100),98.99)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,99,100),100.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,100,0),0.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,100,0),1.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,100,0),50.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,100,0),99.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,100,0),100.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,100,1),0.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,100,1),1.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,100,1),50.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,100,1),99.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,100,1),100.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,100,50),0.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,100,50),1.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,100,50),99.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,100,50),100.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,100,99),0.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,100,99),1.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,100,99),50.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,100,99),99.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,100,99),100.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(0,100,100),0.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(1,100,100),1.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(50,100,100),50.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(99,100,100),99.0)
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,100,100),100.0)

      
       # Path & Coverage Testing 
       # line1
      
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("#","&",1)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("#", "&","$")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("^",10,"^")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("%",10,12)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted(100,"^","%")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted(100,"^",100)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted(15,15,"#")
      self.assertEqual(rawcode_gradecalc.grade_wanted(90,20,88),98.0)
      
      # line2
      
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("!#123","512^","%100")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("&#","@1",100)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("$74",110,"xy#")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("()!",110,500)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted(112,"&X","&xyz")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted(115,"$#",120)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted(512,118,"^!")
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,20,87),152.0)
      
      # line3
      
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("AA","A","A")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("A","Bc",100)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("Z",110,"Z")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("O!",110,500)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted(112,"&X","Y")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted(115,"Mmm",120)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted(512,118,"JK")
      self.assertEqual(rawcode_gradecalc.grade_wanted(100,20,83),168.0)
      
      
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_wanted("","","")

    def test_grade_after_final(self): 
        
        # Normal Boundary Value Tests 
        
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,50,50),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,50,50),25.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,50,50),75.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,50,50),25.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,50,50),74.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,0,50),25.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,100,50),75.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,1,50),25.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,99,50),74.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,50,0),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,50,100),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,50,1),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,50,99),50.0)


      # Robust Boundary Value Tests 
      
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(-1,50,50)
      self.assertEqual(rawcode_gradecalc.grade_after_final(101,50,50),75.5)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(50,-1,50)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,101,50),75.5)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(50,50,-1)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,50,101),50.0)

        
      # Worst Case Boundary Value Tests 

      self.assertEqual(rawcode_gradecalc.grade_after_final(0,0,0),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,0,0),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,50,99),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,0,0),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,0,0),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,0,0),100.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,0,1),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,0,1),0.99)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,0,1),49.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,0,1),98.01)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,0,1),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,0,50),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,0,50),0.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,0,50),49.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,0,50),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,0,99),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,0,99),0.01)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,0,99),0.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,0,99),0.99)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,0,99),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,0,100),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,0,100),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,0,100),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,0,100),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,0,100),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,1,0),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,1,0),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,1,0),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,1,0),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,1,0),100.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,1,1),0.01)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,1,1),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,1,1),49.51)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,1,1),98.02)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,1,1),99.01)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,1,50),0.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,1,50),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,1,50),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,1,50),50.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,1,99),0.99)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,1,99),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,1,99),1.49)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,1,99),1.98)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,1,99),1.99)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,1,100),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,1,100),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,1,100),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,1,100),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,1,100),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,50,0),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,50,0),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,50,0),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,50,0),100.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,50,1),0.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,50,1),1.49)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,50,1),98.51)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,50,1),99.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,50,99),49.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,50,99),49.51)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,50,99),50.49)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,50,99),50.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,50,100),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,50,100),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,50,100),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,50,100),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,99,0),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,99,0),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,99,0),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,99,0),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,99,0),100.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,99,1),0.99)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,99,1),1.98)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,99,1),50.49)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,99,1),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,99,1),99.99)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,99,50),49.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,99,50),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,99,50),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,99,50),99.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,99,99),98.01)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,99,99),98.02)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,99,99),98.51)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,99,99),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,99,99),99.01)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,99,100),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,99,100),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,99,100),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,99,100),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,99,100),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,100,0),0.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,100,0),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,100,0),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,100,0),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,100,0),100.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,100,1),1.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,100,1),1.99)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,100,1),50.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,100,1),99.01)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,100,50),50.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,100,50),50.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,100,50),99.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,100,50),100.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,100,99),99.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,100,99),99.01)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,100,99),99.5)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,100,99),99.99)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,100,99),100.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(0,100,100),100.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(1,100,100),100.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(50,100,100),100.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(99,100,100),100.0)
      self.assertEqual(rawcode_gradecalc.grade_after_final(100,100,100),100.0)
      

         # Path & Coverage Testing 
         # line 1
         
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("$$","$$","$$$")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("&-","m&",50)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("**",100,"m*")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("!",50,50)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(-1,"!","!")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(-1,"!mmm",50)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(-1,50,"!")
      self.assertEqual(rawcode_gradecalc.grade_after_final(88,100,20),90.4)
         
      
        # line 2 
        
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("aa","a90","zzz")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("zz","zz",50)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("a1",100,"m")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("jjjj",50,50)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(-1,"ii","i")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(-1,"aaa",50)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(-1,100,"ooo")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(-1,50,"!")
      self.assertEqual(rawcode_gradecalc.grade_after_final(88,100,20),90.4)   
      
      
      # line 3 
      
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("A","A1","AAA")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("ZZ","ZZ",50)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("aO",100,"O")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("KKKK",50,50)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(-1,"II","I")
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(-1,"PR1",50)
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final(-1,100,"A123")
      self.assertEqual(rawcode_gradecalc.grade_after_final(84,100,20),87.2) 
      
      
      with self.assertRaises(ValueError): 
          rawcode_gradecalc.grade_after_final("","","")
      

if __name__ == '__main__':
    unittest.main()