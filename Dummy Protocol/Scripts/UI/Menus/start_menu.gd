extends Control

@export var main_menu: Control
@export var lobby_menu: Control
@export var settings_menu: Control

func _ready():
	main_menu.visible = true
	lobby_menu.visible = false
	settings_menu.visible = false

func _on_start_button_pressed():
	main_menu.visible = false
	lobby_menu.visible = true
	settings_menu.visible = false

func _on_settings_button_pressed():
	settings_menu.visible = true
	lobby_menu.visible = false


func _on_settings_menu_close_settings():
	settings_menu.visible = false
	lobby_menu.visible = true
