# Item-Catalog-Website

## About


## Tools
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Skills 
- Python
- HTML
- CSS
- Bootstrap
- Flask
- SQLAchemy
- OAuth
- Facebook / Google Login


## REST Endpoints

#### --------------------------------------
#### CRUD
#### --------------------------------------

`/` or `/catalog` - show catalog page with all categories and recently added items
Without Login

<img src="Img for the website/publicCatalog.png" width="800">
With Login

<img src="Img for the website/catalog.png" width="800">

`/catalog/<int:categories_id>/`  - Show items inside the category

<img src="Img for the website/publicCategories.png" width="800">

`/catalog/<int:categories_id>/<int:items_id>` - Show the specific item and the description of it

<img src="Img for the website/movieDetails.png" width="800">


`/catalog/new` - Allows user to create new item

<img src="Img for the website/addNewMovie.png" width="800">

`/catalog/<int:categories_id>/<int:items_id>/edit` - Allows user to edit the specific item

<img src="Img for the website/editMovie.png" width="800">

`/catalog/<int:categories_id>/<int:items_id>/delete` - Allows user to delete the specific item

<img src="Img for the website/deleteMovie.png" width="800">

#### --------------------------------------
#### Login
#### --------------------------------------

`/login` - Allow user to login with Google or Facebook account

<img src="Img for the website/Login.png" width="800">

