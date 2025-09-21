import tkinter as tk
from database import init_db, add_reservation, get_all_reservations,update_reservation,delete_reservation

# إنشاء النافذة الرئيسية
root = tk.Tk()
init_db()
root.title("نظام حجز الرحلات")
root.geometry("420x300")

# عنوان ترحيبي
tk.Label(root, text="مرحبًا في تطبيق حجز الطيران", font=("Arial", 14)).pack(pady=15)


# نافذة الحجز
def open_booking():
    top = tk.Toplevel(root)
    top.title("حجز رحلة")
    top.geometry("400x400")

    tk.Label(top, text="الاسم:").pack(pady=5)
    entry_name = tk.Entry(top, width=30)
    entry_name.pack()

    tk.Label(top, text="رقم الرحلة:").pack(pady=5)
    entry_flight = tk.Entry(top, width=30)
    entry_flight.pack()

    tk.Label(top, text="المغادرة:").pack(pady=5)
    entry_departure = tk.Entry(top, width=30)
    entry_departure.pack()

    tk.Label(top, text="الوصول:").pack(pady=5)
    entry_destination = tk.Entry(top, width=30)
    entry_destination.pack()

    tk.Label(top, text="التاريخ:").pack(pady=5)
    entry_date = tk.Entry(top, width=30)
    entry_date.pack()

    tk.Label(top, text="رقم المقعد:").pack(pady=5)
    entry_seat = tk.Entry(top, width=30)
    entry_seat.pack()

    # زرار الحفظ (جوا open_booking)
    def save_reservation():
        name = entry_name.get()
        flight = entry_flight.get()
        departure = entry_departure.get()
        destination = entry_destination.get()
        date = entry_date.get()
        seat = entry_seat.get()

        add_reservation(name, flight, departure, destination, date, seat)

        print("تم حفظ الحجز:")
        print(name, flight, departure, destination, date, seat)
        tk.Label(top, text="✅ تم حفظ الحجز فى قاعدة البيانات").pack(pady=10)

    tk.Button(top, text="حفظ الحجز", command=save_reservation).pack(pady=20)


# نافذة عرض الحجوزات (مؤقتة)
def open_view():

    top = tk.Toplevel(root)
    top.title("عرض الحجوزات")
    top.geometry("700x400")

    reservations = get_all_reservations()

    if len(reservations) == 0:
        tk.Label(top, text="🚫 لا توجد حجوزات").pack(pady=20)
    else:
        for res in reservations:
            frame = tk.Frame(top)
            frame.pack(fill="x", pady=5)

            # عرض بيانات الحجز
            tk.Label(
                frame,
                text=f"{res[0]} - {res[1]} - {res[2]} - {res[3]} - {res[4]} - {res[5]} - {res[6]}",
                width=90,
                anchor="w"
            ).pack(side="left")

            # زرار الحذف
            def delete_and_refresh(rid=res[0]):
                delete_reservation(rid)
                top.destroy()
                open_view()

            tk.Button(frame, text="❌ حذف", command=delete_and_refresh, fg="red").pack(side="right")

            # زرار التعديل
            def edit_reservation(
                rid=res[0], rname=res[1], rflight=res[2],
                rdep=res[3], rdest=res[4], rdate=res[5], rseat=res[6]
            ):
                edit_win = tk.Toplevel(top)
                edit_win.title("تعديل الحجز")
                edit_win.geometry("400x400")

                # خانات الإدخال
                tk.Label(edit_win, text="الاسم:").pack(pady=5)
                entry_name = tk.Entry(edit_win, width=30)
                entry_name.insert(0, rname)
                entry_name.pack()

                tk.Label(edit_win, text="رقم الرحلة:").pack(pady=5)
                entry_flight = tk.Entry(edit_win, width=30)
                entry_flight.insert(0, rflight)
                entry_flight.pack()

                tk.Label(edit_win, text="المغادرة:").pack(pady=5)
                entry_departure = tk.Entry(edit_win, width=30)
                entry_departure.insert(0, rdep)
                entry_departure.pack()

                tk.Label(edit_win, text="الوصول:").pack(pady=5)
                entry_destination = tk.Entry(edit_win, width=30)
                entry_destination.insert(0, rdest)
                entry_destination.pack()

                tk.Label(edit_win, text="التاريخ:").pack(pady=5)
                entry_date = tk.Entry(edit_win, width=30)
                entry_date.insert(0, rdate)
                entry_date.pack()

                tk.Label(edit_win, text="رقم المقعد:").pack(pady=5)
                entry_seat = tk.Entry(edit_win, width=30)
                entry_seat.insert(0, rseat)
                entry_seat.pack()

                # زرار الحفظ بعد التعديل
                def save_update():
                    update_reservation(
                        rid,
                        entry_name.get(),
                        entry_flight.get(),
                        entry_departure.get(),
                        entry_destination.get(),
                        entry_date.get(),
                        entry_seat.get()
                    )
                    edit_win.destroy()
                    top.destroy()
                    open_view()

                #tk.Button(edit_win, text="تحديث", command=save_update).pack(pady=20)
                tk.Button(frame, text="🗑️", command=delete_and_refresh, fg="red", width=3).pack(side="right", padx=5)

            #tk.Button(frame, text="✏️ تعديل", command=edit_reservation).pack(side="right")
            tk.Button(frame, text="✏️", command=edit_reservation, width=3).pack(side="right", padx=5)

# الأزرار على النافذة الرئيسية
tk.Button(root, text="حجز رحلة", width=20, command=open_booking).pack(pady=8)
tk.Button(root, text="عرض الحجوزات", width=20, command=open_view).pack(pady=8)

# تشغيل الواجهة
root.mainloop()