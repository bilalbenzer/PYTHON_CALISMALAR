from django.db import models
import datetime
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import geopandas as gpd
import os
import zipfile 
from sqlalchemy import *
from geoalchemy2 import Geometry, WKTElement
import glob
import osgeo
from geo.Geoserver import Geoserver
from geo.Postgres import Db
#initializing the library
geo = Geoserver('http://127.0.0.1:8080/geoserver', username='admin', password='geoserver')
db = Db(dbname="geoapp",user="postgres",password="gazi1453",host="localhost",port="5432")

# Create your models here.
#shapefile model
class Shp(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000,blank=True)
    file = models.FileField(upload_to='%Y/%m/%d')
    uploaded_date = models.DateField(default=datetime.date.today,blank=True)

    def __str__(self):
        return self.name

@receiver(post_save,sender=Shp)
def publish_data(sender,instance,created,**kwargs):
    file = instance.file.path
    file_format = os.path.basename(file).split('.')[-1]
    file_name = os.path.basename(file).split('.')[0]
    file_path = os.path.dirname(file)
    name = instance.name
    conn_str= "postgresql://postgres:gazi1453@localhost:5432/geoapp"
    print(file,'file')
    print(file_name)
    print(file_path  )


    #extract zipfile
    with zipfile.ZipFile(file,"r") as zip_ref:
        zip_ref.extractall(file_path)
    os.remove(file) #remove zip file
    shp = glob.glob(r"{}/**/*.shp".format(file_path),recursive=True)    #to (get shp
    print("-------------------------------------")
    print(shp,"shp")
    print("--------------------------------------")
    req_shp = shp[0]
    print(req_shp)
    gdf = gpd.read_file(req_shp)  #make geodataframe
    gdf.head()
    engine = create_engine(conn_str)    #create sql alchemy engine to use 

    gdf.to_postgis(name,engine,"public",
            if_exists='replace',
            index=False)   #post gdf to postgresql
    for s in (shp):
        os.remove(s)
    
    '''
    Publish Shp To  Geoserver Using Geoserver Rest
    '''
    geo.create_featurestore(store_name='gisweb', workspace='gisweb', db='geoapp', host='localhost', pg_user='bilalbenzer',
                        pg_password='gazi1453', schema = 'data'),
    geo.publish_featurestore(workspace='gisweb', store_name='gisweb', pg_table=name)



@receiver(post_delete,sender=Shp)
def delete_data(sender,instance,**kwargs):
    db.delete_table(table_name=instance.name, schema="public")
    geo.delete_layer(instance.name,"geoapp")

    