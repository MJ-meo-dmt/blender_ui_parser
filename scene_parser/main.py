

class EggSceneParser():

	def __init__(self, _game):

		# 
		self.game = _game

		# Keep track of all the generated objects (parsed from egg file)
		self.levelName = ""
		self.levelDesc = ""
		self.objCount = 0

		# Player related
		self.playerSpawnPoint = (0, 0, 0)

		# Object related
		self.pickupObjects = {} # Objects that are pickable
		self.objects = {} # Most objects that can move
		self.sensors = {} # All sensors "buttons", triggers"
		self.lifts = {}
		self.doors = {}

		# Parent Node paths
		self.parentRender = ""
		self.parentPhysics = ""

		# Root Egg file
		self.eggRootModel = ""

		## Object Types ##
		self.objectTypes = {}


	def parseEggFile(self, _eggPath):

		root = loader.loadModel(_eggPath)
		self.eggRootModel = root

		# Fetch objects in egg file
		objects = root.findAllMatches("**")

		for obj in objects:
			for objType in self.objectTypes:
				if obj.hasTag(objType):
					self.buildObject(obj, objType, root)


	def buildObject(self, _obj, _type, _rootModel):
		self.objectTypes[_type](_obj, _rootModel)