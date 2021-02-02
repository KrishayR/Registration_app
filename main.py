import tkinter as tk 



class Person:

  def __init__(self,firstName,lastName):
    self.firstName = firstName
    self.lastName = lastName
    self.address = Address()

class Address:

  def __init__(self):
    self.street = ""
    self.city = ""
    self.zip = 0

persons = []

root = tk.Tk()
root.title("Registration App")

personalInfo_frame = tk.Frame(
                              root,
                              width=800,
                              height=200,
                              bg="#97ff05"
)
personalInfo_frame.pack()

address_frame = tk.Frame(
                              root,
                              width=800,
                              height=200,
                              bg="#b0ff05"
)
address_frame.pack()

personalInfo_label = tk.Label(
                              personalInfo_frame,
                              text="Personal Information",
                              bg="#97ff05",
                              fg="#000000"
)
personalInfo_label.grid(row=0,column=0)

firstName_label = tk.Label(
                          personalInfo_frame,
                          text="First name",
                          bg="#97ff05"
)
firstName_label.grid(row=1,column=0)

firstName_Entry = tk.Entry(
                          personalInfo_frame,
                          width=100
)
firstName_Entry.grid(row=1,column=1)

lastName_label = tk.Label(
                          personalInfo_frame,
                          text="Last name",
                          bg="#97ff05"
)
lastName_label.grid(row=2,column=0)

lastName_Entry = tk.Entry(
                          personalInfo_frame,
                          width=100
)
lastName_Entry.grid(row=2,column=1)

address_label = tk.Label(
                          address_frame,
                          text="Address",
                          bg="#b0ff05"
)
address_label.grid(row=0,column=0)

street_label = tk.Label(
                          address_frame,
                          text="Street",
                          bg="#b0ff05"
)
street_label.grid(row=1,column=0)

street_Entry = tk.Entry(
                          address_frame,
                          width=108
)
street_Entry.grid(row=1,column=1)

city_label = tk.Label(
                          address_frame,
                          text="City",
                          bg="#b0ff05"
)
city_label.grid(row=2,column=0)

city_Entry = tk.Entry(
                          address_frame,
                          width=108
)
city_Entry.grid(row=2,column=1)

zip_label = tk.Label(
                          address_frame,
                          text="Zip",
                          bg="#b0ff05"
)
zip_label.grid(row=3,column=0)

zip_Entry = tk.Entry(
                          address_frame,
                          width=108
)
zip_Entry.grid(row=3,column=1)

def registerPerson():
  firstName = firstName_Entry.get()
  lastName = lastName_Entry.get()

  street = street_Entry.get()
  city = city_Entry.get()
  zipCode = zip_Entry.get()

  person = Person(firstName,lastName)
  person.address.street = street
  person.address.city = city
  person.address.zip = zipCode

  global persons
  persons.append(person)

  firstName_Entry.delete(0,tk.END) 
  lastName_Entry.delete(0,tk.END)
  city_Entry.delete(0,tk.END)
  street_Entry.delete(0,tk.END)
  zip_Entry.delete(0,tk.END)

submit_button = tk.Button(
                          root,
                          text="Submit",
                          command=registerPerson
)
submit_button.pack(side=tk.RIGHT)

def printResults():
  global persons
  for i,person in enumerate(persons):
    print("--- Person (%d) ---" % i)
    print("First name: ", person.firstName)
    print("Last name: ", person.lastName)
    print("--- Address ---")
    print(person.address.street)
    print("{0} {1}".format(person.address.city,person.address.zip))
    print()

results_button = tk.Button(
                          root,
                          text="Results",
                          command=printResults
)
results_button.pack(side=tk.RIGHT)


root.mainloop()


