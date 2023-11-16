#Para ejecutar:
#1. Ir a la carpeta backend
#2. SET FLASK_APP=server
#3. SET FLASK_ENV=development
#4. flask run

from unicodedata import name
from flask import(
    Flask,
    abort,
    jsonify,
    request
)

from werkzeug.security import check_password_hash, generate_password_hash

from flask_cors import CORS

from models import setup_db, Category, Post, User

#Paginación

TODOS_PER_PAGE=10000000000000

def paginate(request,selection,isDescendent):
    if isDescendent:                #Cuando se crea con CURL, muestra solo los últimos recursos creados
        start = len(selection)-TODOS_PER_PAGE
        end = len(selection)
    
    else:
        page=request.args.get('page',1,type=int)  #request.args.get trae los recursos especificados por el usuario por query parameters (luego del '?' en el url viene los query parameters)
        start = (page-1)*TODOS_PER_PAGE
        end = start+TODOS_PER_PAGE
    
    resources = [resource.format() for resource in selection]
    current_resources= resources[start:end]
    return current_resources


#API

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, origins="*", max_age=10)
    
    @app.after_request
    def after_resquest(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/login', methods=['POST'])
    def login():
        username = request.get_json()['username']
        print("Username submited:", username)
        password = request.get_json()['password']
        print("Password submited:", password)
        
        user = User.query.filter(User.username == username).first()
        
        if user is not None:
            psw = check_password_hash(user.password, password)
            print("Password match:", psw)
        else:
            print("User not found")

        if user is None or psw is False:
            abort(403)
        else:
            return jsonify({
                'success': True,
                'profile': {
                    'username': username,
                    'user_id': user.id,
                    'password': user.password,
                }
            })

    @app.route('/posts', methods=['GET'])      
    def get_posts():
        selection=Post.query.order_by('id').all()
        posts=paginate(request,selection,False)
      
        if (len(posts))==0:
            abort(404) 

        return jsonify({    #Las claves estarán ordenadas en orden alfabético
            'success': True,
            'posts': posts,
            'total_posts': len(selection)
        })

    @app.route('/posts', methods=['POST'])
    def create_post():
        print("Entra a POST")
        body=request.get_json() 
        print("info:")
        author=body.get('author',None)
        title=body.get('title',None)
        texto=body.get('body',None)
        category_id=body.get('category_id',None)
        search = body.get('search',None)

        if search:
            selection = Post.query.order_by('id').filter(Post.title.like('%{}%'.format(search))).all()

            if len(selection)==0:
                abort(404)
            else:
                posts=paginate(request,selection,False)
                return jsonify({
                    'success':True,
                    'posts':posts,
                    'coincidencias':len(selection)
                })

        if author is None or title is None or category_id is None or texto is None:
            abort(422)

        post = Post(author=author,title=title,body=texto,category_id=category_id)
        post.insert()
        new_post_id=post.id
        new_post_title=post.title
        
        selection = Post.query.order_by('id').all()
        current_posts=paginate(request,selection,True)

        
        return jsonify({
            'success': True,
            'created': new_post_id,
            'title': new_post_title,
            'posts': current_posts,
            'total_posts': len(selection)
        })

    @app.route("/posts/<post_id>",methods=["PATCH"]) 
    def update_post(post_id):
        error_404=False
        error_422=False
        try:
            post = Post.query.filter(Post.id==post_id).one_or_none()

            if post is None:
                error_404=True
                abort(404)
                
            body = request.get_json()

            if 'author' in body:   
                id_nuevo_autor = body.get('author')
                autores = User.query.filter(User.id==id_nuevo_autor).one_or_none()
                if autores is None:
                    error_422=True
                    abort(422)
                else:
                    post.author = body.get('author')

            if 'title' in body:
                post.title = body.get('title')

            if 'body' in body:
                post.body = body.get('body')

            if 'category_id' in body:      
                id_nueva_categoria = body.get('category_id')
                categories = Category.query.filter(Category.id==id_nueva_categoria).one_or_none()
                if categories is None:
                    error_422=True
                    abort(422)
                else:
                    post.category_id = body.get('category_id')
            
            post.update()

            return jsonify({
                'success':True,
                'id': post_id
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            elif error_422:
                abort(422)
            else:
                abort(500)

    @app.route('/posts/<post_id>',methods=['DELETE'])  
    def delete_post(post_id):
        error_404=False
        try:
            post = Post.query.filter(Post.id==post_id).one_or_none()
            if post is None:
                error_404=True
                abort(404)
            
            post.delete()

            selection = Post.query.order_by('id').all()
            posts = paginate(request,selection,True)

            return jsonify({
                'success': True,
                'deleted': post_id,
                'posts': posts,
                'total_posts': len(selection)
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)  
            else:
                abort(500)
        
    #Rutas para users: Funcionan todas


    @app.route('/users', methods=['GET'])       #Sí funciona
    def get_users():
        selection=User.query.order_by('id').all()
        users=paginate(request,selection,False)
        #return posts no es una respuesta válida porque no se puede retornar una lista, entonces:
        if (len(users))==0:
            abort(404) #devuelve un html 404, no está estandarizado todavía.
        print("Entra a GET")
        return jsonify({ #Las claves estarán ordenadas en orden alfabético
            'success': True,
            'users': users,  #Ahora el objeto ya está formateado a json porque fue formateado en paginate
            'total_users': len(selection)
        })

    @app.route('/users', methods=['POST']) 
    def create_user():
        print("Entra a POST")
        info=request.get_json()  
        print("info:")
        username=info.get('username',None)
        password=info.get('password',None)
        search = info.get('search',None)

        if search:
            selection = User.query.order_by('id').filter(User.username.like('%{}%'.format(search))).all()

            if len(selection)==0:
                abort(404)
            else:
                users=paginate(request,selection,False)
                return jsonify({
                    'success':True,
                    'users':users,
                    'coincidencias':len(selection)
                })

        if username is None or password is None:
            abort(422)

        user = User(username=username, password=generate_password_hash(password))
        user.insert() #Metodo creado en models.py para commitear un post
        new_user_id=user.id
        new_user_username=user.username
        
        selection = User.query.order_by('id').all()
        current_users=paginate(request,selection,True)

        
        return jsonify({
            'success': True,
            'created': new_user_id,
            'username': new_user_username,
            'users': current_users,
            'total_users': len(selection)
        })

    @app.route("/users/<user_id>",methods=["PATCH"])  
    def update_user(user_id):
        error_404=False
        try:
            user = User.query.filter(User.id==user_id).one_or_none()

            if user is None:
                error_404=True
                abort(404)
                
            body = request.get_json()
            if 'username' in body:
                user.username = body.get('username')
            
            if 'password' in body:
                user.password = body.get('password')
                user.password = generate_password_hash(user.password)
            
            user.update()

            return jsonify({
                'success':True,
                'id': user_id
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)

    @app.route('/users/<user_id>',methods=['DELETE'])   
    def delete_user(user_id):
        error_404=False
        try:
            user = User.query.filter(User.id==user_id).one_or_none()
            if user is None:
                error_404=True
                abort(404)
            
            user.delete()

            selection = User.query.order_by('id').all()
            users = paginate(request,selection,True)

            return jsonify({
                'success': True,
                'deleted': user_id,
                'users': users,
                'total_users': len(selection)
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)

    

    @app.route('/categories', methods=['GET'])       
    def get_categories():
        selection=Category.query.order_by('id').all()
        categories=paginate(request,selection,False)
        
        if (len(categories))==0:
            abort(404) 
        print("Entra a GET")
        return jsonify({ #Las claves estarán ordenadas en orden alfabético
            'success': True,
            'categories': categories,  
            'total_categories': len(selection)
        })

    @app.route('/categories', methods=['POST']) 
    def create_category():  
        info=request.get_json()
        name_category=info.get('name_category',None)
        search = info.get('search',None)

        if search:
            selection = Category.query.order_by('id').filter(Category.name_category.like('%{}%'.format(search))).all()

            if len(selection)==0:
                abort(404)
            else:
                categories=paginate(request,selection,False)
                return jsonify({
                    'success':True,
                    'categories':categories,
                    'coincidencias':len(selection)
                })
        

        if name_category is None:
            abort(422)

        category = Category(name_category=name_category)
        category.insert() 
        new_category_id=category.id
        new_category_name=category.name_category
        
        selection = Category.query.order_by('id').all()
        current_categories=paginate(request,selection,True)

        
        return jsonify({
            'success': True,
            'created': new_category_id,
            'name': new_category_name,
            'categories': current_categories,
            'total_categories': len(selection)
        })

    @app.route("/categories/<category_id>",methods=["PATCH"])   #Funciona
    def update_category(category_id):
        error_404=False
        try:
            category = Category.query.filter(Category.id==category_id).one_or_none()

            if category is None:
                error_404=True
                abort(404)
                
            body = request.get_json()
            if 'name_category' in body:
                category.name_category = body.get('name_category')
            
            category.update()

            return jsonify({
                'success':True,
                'id': category_id
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)

    @app.route('/categories/<category_id>',methods=['DELETE'])    #Funciona
    def delete_category(category_id):
        error_404=False
        try:
            category = Category.query.filter(Category.id==category_id).one_or_none()
            if category is None:
                error_404=True
                abort(404)
            
            category.delete()

            selection = Category.query.order_by('id').all()
            categories = paginate(request,selection,True)

            return jsonify({
                'success': True,
                'deleted': category_id,
                'categories': categories,
                'total_categories': len(selection)
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            else:
                abort(500)


    #Manejo de errores

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'code': 404,
            'message': 'resource not found'
        }),404

    @app.errorhandler(422)
    def unprocessable (error):
        return jsonify({
            'success': False,
            'code': 422,
            'message': 'Unprocessable'
        }), 422

    @app.errorhandler(500)
    def not_found(error):
        return jsonify({
            'success': False,
            'code': 500,
            'message': 'internal server error'
        }),500

    @app.errorhandler(403)
    def not_found(error):
        return jsonify({
            'success': False,
            'code': 403,
            'message': 'forbidden'
        }),403
    

    return app