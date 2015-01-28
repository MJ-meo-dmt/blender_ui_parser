

class BaseObject():

	# Basic Object props
	name = ""
	modelPath = ""
	isDynamic = False
	sendEvent = ""
	recvEvent = ""
	customScript = ""
	state = False
	pickable = False
	lookAt = ""

	# Physics related props
	moveForce = 0.0
	jumpForce = 0.0
	moveAmount = 0.0
	moveAxis = ''
	rotateAmount = 0.0
	rotateAxis = ''
	gravity = (0.0, 0.0, 0.0)
	isCollisionMesh = False
	isBulletPlane = False

	# Light types
	color = (0, 0, 0, 0)
	hpr = (0, 0, 0)

	# Task types
	priority = 100 # more is less important


