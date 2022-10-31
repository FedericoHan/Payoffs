    
    '''given a few securities , produce quick payoff vs pure linear '''
    
    def __init__(self, range_low, range_high, step, k , pos, callput, forward, lev):
        
        self.range_low = range_low
        self.range_high = range_high
        self.step = step
        self.k = k 
        self.pos = pos 
        self.callput = callput 
        self.forward = forward
        self.lev = lev  #leverage if any in underlying possy, if none just -1 or 1 for short or long
    def _create_range_(self):
        '''create x asis for payoff '''
        x =np.arange(self.range_low, self.range_high, self.step)
        return x 
 
    def _create_payoff_(self):
        '''create option payoffs '''
        
        x = self._create_range_()
      
        n = len(self.k)
        y = [0]*n #init payoffs array
       
        for i in range(n):
            if self.callput[i] == 'put':
                y[i] = np.where( (self.k[i] - x)>0, (self.k[i]-x)*self.pos[i], 0)
            else:
                y[i] = np.where( (x- self.k[i])>0, (x - self.k[i])*self.pos[i], 0)
            #debug print(y[i])
        return y
    
    def _create_linear_payoff_(self):
        #forward wehre buy or sell underlying, lev is  +1 if long
        x = self._create_range_()
        return (x- self.forward)* self.lev
    
    def draw_payoff(self):
        
        #first sum option payoffs
        payoff_option = self._create_payoff_()
        payoff_option_sum = [0]
        for i in range(len(payoff_option)):
            
            payoff_option_sum += payoff_option[i]

        
        #then get linear payoffs
        payoff_linear = self._create_linear_payoff_()
        
        #then plot together 
        plt.plot(self._create_range_(), payoff_option_sum, label = 'payoff_options')
        plt.plot(self._create_range_(), payoff_linear , label = 'payoff_linear')
        plt.legend()
        plt.grid(True)
        plt.plot(figsize = (10,5))
        plt.show()
        
 
        return payoff_option_sum

if __name__ == '__main__': 
    
    #stonk price
    k2 = [108, 107, 115, 117.5]
    
    pos2 = [0, 1, 2, -3]
    
    callput2= ['put', 'put', 'call', 'call']

    bunny2 = Payoffs(104, 120, 0.5, k2, pos2, callput2, 110, 1)


    b = bunny2.draw_payoff()
    b