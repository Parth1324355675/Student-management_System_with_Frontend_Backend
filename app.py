import streamlit as st
from student_manager import StudentManager
import pandas as pd

manager = StudentManager()

st.title("🎓 Student Management System")

menu = st.sidebar.selectbox(
    "Choose Option",
    ["Add Student", "Display Students", "Search Student",
     "Update Student", "Delete Student", "Export CSV", "Report","Dashboard"]
)

# ---------------- ADD ----------------
if menu == "Add Student":
    st.header("Add Student")

    name = st.text_input("Enter Name")
    roll = st.number_input("Enter Roll", step=1)
    marks = st.number_input("Enter Marks", step=1.0)

    if st.button("Add"):
        manager.add_student(int(roll), name, float(marks))
        st.success("Student Added")

# ---------------- DISPLAY ----------------
elif menu == "Display Students":
    st.header("All Students")

    if len(manager.students) == 0:
        st.warning("No students found")
    else:
        data = [{"Roll": s.roll, "Name": s.name, "Marks": s.marks} for s in manager.students]
        df = pd.DataFrame(data)
        st.dataframe(df)

# ---------------- SEARCH ----------------
elif menu == "Search Student":
    st.header("Search Student")

    key = st.text_input("Enter Roll or Name")

    if st.button("Search"):
        # found = False
        for s in manager.students:
            if str(s.roll) == key or s.name.lower() == key.lower():
                st.success(f"Found: {s}")
                found = True
                break
        if not found:
            st.error("Student not found")

# ---------------- UPDATE ----------------
elif menu == "Update Student":
    st.header("Update Student")

    roll = st.number_input("Enter Roll", step=1)
    name = st.text_input("New Name")
    marks = st.number_input("New Marks", step=1.0)

    if st.button("Update"):
        for s in manager.students:
            if s.roll == int(roll):
                s.name = name
                s.marks = marks
                manager.save_students()
                st.success("Updated successfully")
                break
        else:
            st.error("Student not found")

# ---------------- DELETE ----------------
elif menu == "Delete Student":
    st.header("Delete Student")

    roll = st.number_input("Enter Roll", step=1)

    if st.button("Delete"):
        for s in manager.students:
            if s.roll == int(roll):
                manager.students.remove(s)
                manager.save_students()
                st.success("Deleted successfully")
                break
        else:
            st.error("Student not found")

# ---------------- EXPORT ----------------
elif menu == "Export CSV":
    st.header("Export Data")

    if st.button("Export"):
        manager.export_to_csv()
        st.success("Exported to students.csv")

    if st.button("Download"):
        data = [{"Roll": s.roll, "Name": s.name, "Marks": s.marks} for s in manager.students]
        df = pd.DataFrame(data)

        csv = df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="students.csv",
            mime="text/csv"
        )

# ---------------- REPORT ----------------
elif menu == "Report":
    st.header("Report")

    if len(manager.students) == 0:
        st.warning("No data")
    else:
        total = len(manager.students)
        avg = sum(s.marks for s in manager.students) / total
        highest = max(manager.students, key=lambda s: s.marks)
        lowest = min(manager.students, key=lambda s: s.marks)

        st.write(f"Total Students: {total}")
        st.write(f"Average Marks: {avg}")
        st.write(f"Topper: {highest.name} ({highest.marks})")
        st.write(f"Lowest: {lowest.name} ({lowest.marks})")


elif menu == "Dashboard":
    st.header("📊 Student Dashboard")


    if len(manager.students) == 0:
        st.warning("No data available")
    else:
        data = [{"Roll": s.roll, "Name": s.name, "Marks": s.marks} for s in manager.students]
        df = pd.DataFrame(data)

        # 🔹 Top metrics (in columns)
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Students", len(df))
        col2.metric("Average Marks", round(df["Marks"].mean(), 2))
        col3.metric("Highest Marks", df["Marks"].max())
        col4.metric("Lowest Marks", df["Marks"].min())

        st.divider()

        # 🔹 Table
        st.subheader("📋 Student Data")
        st.dataframe(df, use_container_width=True)


        st.divider()

        # 🔹 Charts
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Marks Chart")
            st.bar_chart(df.set_index("Name")["Marks"])
            st.divider()

        with col2:
            st.subheader("🥧 Pass vs Fail")

            df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")


            st.write(df["Status"].value_counts())

            
            st.bar_chart(df["Status"].value_counts())