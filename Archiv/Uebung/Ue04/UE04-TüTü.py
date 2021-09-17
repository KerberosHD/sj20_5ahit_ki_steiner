#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Train:
    _passengersList = []
          
    def stepIn(self, pas):
        self._passengersList.append(pas)
    
    def stepOut(self, pas):
        self._passengersList.remove(pas)
        
    def showPassengers(self):
        for passenger in self._passengersList:
            passenger.show_passengers()

    def delete_passenger_list(self):
        self._passengersList.clear()
class Passenger:
    
    _first_name = ""
    _last_name = ""
    _valid_ticket = False
    
    def __init__(self, first_name, last_name, valid_ticket):
        self._first_name = first_name
        self._last_name = last_name
        self._valid_ticket = valid_ticket
    
    def show_first_name(self):
        return  self._get_first_name()
    
    def _get_first_name(self):
        return self._first_name
    
    def show_last_name(self):
        return  self._get_last_name()
    
    def _get_last_name(self):
        return self._last_name
    
    def show_valid_ticket(self):
        return  self._get_valid_ticket()
    
    def _get_valid_ticket(self):
        return self._valid_ticket
    
    def set_valid_ticket(self):
          self._valid_ticket = not self._valid_ticket
    
    def show_passengers(self):
        print("Passengers: Firstname: %s Lastname: %s Ticket: %s" %(self._first_name,self._last_name,self._valid_ticket))


# In[4]:


class RailJet(Train):
        
    def stepIn(self, pas):
        if(pas._valid_ticket):
               Train.stepIn(self, pas)
        else:
            print("%s: You don't have a ticket" %(pas._last_name))
            
    def stepOut(self, pas):
        Train.stepOut(self, pas)
        pas.set_valid_ticket()
    
    
class InterCity(Train):
    
    _ice_category = ""
    
    def __init__(self, ice_category):
        self._ice_category = ice_category
        
    def show_ice_category(self):
        return  self._get_ice_category()
    
    def _get_ice_category(self):
        return self._ice_category
    


# In[13]:


rail_jet = RailJet()
person1 = Passenger("Tobias", "Steiner", True)
person2 = Passenger("Nico", "Zelinsky", False)
person3 = Passenger("Max", "Huber", True)

rail_jet.stepIn(person1)
rail_jet.stepIn(person2)
rail_jet.stepIn(person3)
rail_jet.showPassengers()
rail_jet.stepOut(person1)
print()
rail_jet.showPassengers()
print()
person1.show_passengers()


inter_city1 = InterCity("ICE4711")
inter_city2 = InterCity("ICE4131")
inter_city3 = InterCity("ICE3731")
print(inter_city1.show_ice_category())

rail_jet.delete_passenger_list()

