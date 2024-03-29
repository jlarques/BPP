class Vehicle(object):
    '''
    The Vehicle object contains lots of vehicles
    :param arg: The arg is used for ...
    :type arag: str
    :param `*args`: The variable arguments are used for ...
    :param `**kwargs+: The keyword arguments are used for ...
    :ivar arg: This is where we store arg
    :vartype arg: str
    '''
    def __init__(self, arg, *args, **kwargs):
        self.arg=arg
    
    def cars(self, distance, destination):
        '''We can't travel a certain distance in vehicles without fules, so here's the fuels
        
        :param distance: The amount of distance traveled
        :type amount: int
        :param bool destinationReached: Should the fuels be refilled to cover required distance
        :raises: class: `RuntimeError`: Out of fuel
        
        :returns: A car mileage
        :rtype: Cars
        '''
        pass
    