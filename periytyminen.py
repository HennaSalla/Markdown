# PERIYTYMINEN INHERITANCE
# ========================

# KIRJASTOT JA MODUULIT
# ---------------------
# import oliot # Tuodaan koko oliot.py moduulin sisältö
import datetime
from oliot import Student # Tuodaan oliot moduulista Student-luokka

# YLILUOKKA ELI ÄITILUOKKA (SUPER / PARENT CLASS)
# -----------------------------------------------
class Person():
    """Common class for all person in Raseko"""
    def __init__(self, givenName: str, surName: str):
        """Creates a Person object

        Args:
            egivenName (str): A first name
            sukunimi (str): A last name
        """
        self.givenName = givenName
        self.surName = surName

    def calculateAge3(self, isoBirthday: str) -> float:
        birthday = datetime.datetime.fromisoformat(isoBirthday)
        age = datetime.datetime.now() - birthday
        ageInYears = age.days / 365
        return ageInYears

    # Staattinen metodi, joka laskee iän.Staattisessa metodissa ei luoda oliota laikaan vaan metodia voi käyttää suoraan luokasta käsin 
    @staticmethod
    def calculateAge(birthday):
            """Calculates studnet's current age in full years

            Returns:
                float: age in years
            """
            birthDay = datetime.datetime.fromisoformat(birthday)
            age = datetime.datetime.now() - birthDay
            ageInYears = age.days / 365
            return round(ageInYears)
    
    # Luokkametodi on myös saattinen, eli ei vaadi olion muodostamista
    # Huomaa luokkaan viittaava cls, joka korvaa perinteisen self:n
    @classmethod
    def caculateAge2(cls, birthday):
            """Calculates studnet's current age in full years

            Returns:
                float: age in years
            """
            birthDay = datetime.datetime.fromisoformat(birthday)
            age = datetime.datetime.now() - birthDay
            ageInYears = age.days / 365
            return round(ageInYears)
    


# ALILUOKKA ELI LAPSILUOKKA (SUB / CHILD CLASS)
# ---------------------------------------------
class RasekoStudent(Person):
    """The students class, inherits The Person class"""
    def __init__(self, givenName: str, surName: str, studentNumber: str):
        """Creates a student object

        Args:
            giveName (str): Student's first name
            surName (str): Student's last name
            studentNumber (str): Student's ID
        """
        super().__init__(givenName, surName) # Määritellään tapahtuvaksi yliluokan mukaan
        self.studentNumber = studentNumber # Ei määritelty yliluokassa

class RasekoTeacher(Person):
    """Create a teacher inheriting the Person class

    Args:
        Person (class): Name of the super class
    """
    def __init__(self, givenName: str, surName: str, group: list[str]):
        """Creates a teacher objects

        Args:
            givenName (str): Teacher's given name
            surName (str): Teacher's surname
            group (list[str]): List of student goups
        """
        super().__init__(givenName, surName)
        self.group = group

    

if __name__ == "__main__":
    rasekoStudent = RasekoStudent('Jonne', 'Janttari', '456543')
    print(rasekoStudent.surName)  

    luokat = ['Tivi23A', 'TiVi23B', 'TiVi20oa']
    rasekoTeacher = RasekoTeacher('Markku', 'Kynsijärvi', luokat)
    print(f'{rasekoTeacher.givenName} opettaa ryhmiä {rasekoTeacher.group}')

    # Luodaan moduulista oliot.py Student-olio
    student = Student('Tuittu Kiukkunen', 'Auto22B', '2007-10-23')
    print(f'{student.name} on {student.calculateAge()}')

    ika = Person.calculateAge('2008-03-22')
    print(ika)

    ika2 = Person.caculateAge2('1978-12-10')
    print(ika2)

    person1 = Person('Calle', 'Keckelbergs')
    ika3 = person1.calculateAge3('2009-10-22')
    print(f'Henkilön {person1.givenName} ikä on {ika3} vuotta')