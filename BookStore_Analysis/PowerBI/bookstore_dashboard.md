#   Bookstore Dashboard - Data Modeling 

##  Model
- **Fact Table**: `books_clean_with_authors_ids_sales`  
  (book_id, title, price, sales_units, rating, **author_id**)  
- **Dimension Table**: `authors`  
  (**author_id**, author_name)  


##  Why this design?
- Simple & fast for DAX + queries.  
- Easy to extend with new dimensions (publishers, genres, dates).  
- Supports both book-level and author-level analysis.  

---

# 📊 Measures & Visuals

##  Measures
```DAX
Total Revenue = SUMX(
    books_clean_with_authors_ids_sales,
    books_clean_with_authors_ids_sales[price] * books_clean_with_authors_ids_sales[sales_units]
)

- **Num of Books**  
```DAX
Num of Books = DISTINCTCOUNT(books_clean_with_authors_ids_sales[title])

```
## 📊 Dashboard Visuals

- **Cards**: Total Revenue, Number of Books → quick KPIs  
- **Table**: Book details (title, price, rating, cover)  
- **Line Charts**: Best & Worst Selling Books → identify performance  
- **Pie Charts**: Most & Least Published Authors → author productivity  
- **Slicer**: Filter by Book Title → interactivity  


 ## Dashboard & Data Model Links
 
in [Google Drive](https://drive.google.com/file/d/1imNknTjgaPTZrPDHNSDtJH23fJtN7ugj/view?usp=sharing)

in [Power BI Service (Cloud)](https://app.powerbi.com/groups/abc33743-11f1-4cc6-a0f8-0af59e0e9a8c/reports/a872ad24-ea6f-40bd-988d-0b708a01832d/9cbd29265d740196aaf2?experience=power-bi)
