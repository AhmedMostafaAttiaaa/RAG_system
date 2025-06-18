from .BaseDataModel import BaseDataModel
from .db_schemes import Asset
from .enums.DataBaseEnum import DataBaseEnum
from bson import ObjectId


class AssetModel(BaseDataModel):
    
    
    def __init__(self, db_client:object):
        super().__init__(db_client=db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_ASSET_NAME.value]


    @classmethod # static method to deal with the __init__ without being async and the init__collection without calling it with #await    
    async def create_instance(cls, db_client: object):
        instance = cls(db_client)
        await instance.init_collection()
        return instance    


    async def init_collection(self):
        all_collections = await self.db_client.list_collection_names()
        if DataBaseEnum.COLLECTION_ASSET_NAME.value not in all_collections:
            self.collection = self.db_client[DataBaseEnum.COLLECTION_ASSET_NAME.value]
            indexes = Asset.get_indexes() ###
            for index in indexes:
                await self.collection.create_index(
                    index["key"],
                    name=index["name"],
                    unique=index["unique"]
                )

    async def create_asset(self, asset: Asset):

        result = await self.collection.insert_one(asset.dict(by_alias=True, exclude_unset=True))            
        asset._id = result.inserted_id

        return asset
    

    async def get_all_project_assets(self, asset_project_id: str):
        return await self.collection.find(
            {
                "asset_project_id": asset_project_id



            }
        )

