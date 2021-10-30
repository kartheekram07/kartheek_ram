class ALU():

    carry_flag=0

    def ADD(self,source,dest):
        self.source=source
        self.dest=dest
        self.source=self.source+self.dest
        return self.source


    def ADD(self,source,dest1,dest2):
        self.source=source
        self.dest1=dest1
        self.dest2=dest2
        self.source=self.dest2+self.dest1
        return self.source


    def SUB(self,source,dest):
        self.source=source
        self.dest=dest
        self.source=self.source-self.dest
        return self.source

    def SUB(self,source,dest1,dest2):
        self.source=source
        self.dest1=dest1
        self.dest2=dest2
        self.source=self.dest1-self.dest2
        return self.source
        


    def MUL(self,source,dest):
        self.source=source
        self.dest=dest
        self.source=self.source*self.dest
        return self.source

    def DIV(self,source,dest):
        self.source=source
        self.dest=dest
        self.source=source//dest
        return self.source
    
    def INC(self,op):
        self.op=op
        return op+1
    
    def DEC(self,op):
        self.op=op
        return op-1


    def LOAD(self,source):
        self.source=source
        return self.source    # here it should load from memory(How??)


    def STORE(self,source):
        self.source=source
        pass                   # Here it should be stored to memory(may be accessed from one part of memory)


    def AND(self,op1,op2):
        self.op1=bin(op1)
        self.op2=bin(op2)
        return op1 and op2



    def OR(self,op1,op2):
        self.op1=bin(op1)
        self.op2=bin(op2)
        return op1 and op2



    def NOT(self,op1):
        self.op1=bin(op1)
        return ~self.op1
    
    def XOR(self,op1,op2):
        self.op1=bin(op1)
        self.op2=bin(op2)
        return op1^op2

    def cmp(self,op1,op2):
        self.op1=op1
        self.op2=op2
        if(self.op1==self.op2):
            self.carry_flag=0
        if(self.op1<self.op2):
            self.carry_flag=-1
        if(self.op1<=self.op2):
            self.carry_flag=1
        
        return self.carry_flag
        
        


    



    