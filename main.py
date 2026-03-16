import tkinter as tk
from employee import add_employee



root = tk.Tk()
root.title("Helpdesk Ticket System")
root.geometry("400x500")

# Frame container
container = tk.Frame(root)
container.pack(fill="both", expand=True)

def employee_page():
    page = tk.Toplevel(root)
    page.title("Helpdesk Ticket System")
    page.geometry("500x500")

    tk.Label(page, text="Employee No.").pack()
    emp_no = tk.Entry(page)
    emp_no.pack()

    tk.Label(page, text="First Name").pack()
    first_name = tk.Entry(page)
    first_name.pack()

    tk.Label(page, text="Last Name").pack()
    last_name = tk.Entry(page)
    last_name.pack()

    def save():
        add_employee(emp_no.get(), first_name.get(), last_name.get())

    tk.Button(page, text="Add Employee", command=save).pack(pady=10)

tk.Button(root, text="Employees", width=20, command=employee_page).pack(pady=10)

root,tk.mainloop()