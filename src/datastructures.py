"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10,14,3]   
            },
             {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]   
            }]


    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):

        if "id" not in member:
            member["id"] = self._generate_id()

        if "first_name" not in member or "age" not in member or "lucky_numbers" not in member:
            raise ValueError("Faltan campos requeridos: first_name, age, lucky_numbers")
        
        if not isinstance(member["age"], int) or member["age"] <= 0:
            raise ValueError("El campo age debe ser un número entero positivo")

        if not isinstance(member["lucky_numbers"], list) or not all(isinstance(n, int) for n in member["lucky_numbers"]):
            raise ValueError("lucky_numbers debe ser una lista de enteros")        
        self._members.append(member)
    
        return member

    def delete_member(self, id):
        
        member = [item for item in self._members if item["id"] == id]
        if member:
            self._members.remove(member[0])
            return True
        return False

    def get_member(self, id):
        
        return next((item for item in self._members if item["id"] == id), [])

    def get_all_members(self):
        return self._members