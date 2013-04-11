/**
 * @author Amaury Pernette
 */

viewer = {

	// Urls
	config_url : '/config.json',

	// Id/class Html
	id_slideshow : '#slideshow',
	cl_slide : '.slide',

	// Screen size
	width : null,
	height : null,

	// Options
	opts : {
		fx : 'fade',
		delay : 4000,
		timeout : 5000,
		speed : 1000
	},

	// Refs of displayed images
	// use to cache data
	images : [],
	nb_img_to_load: 0,
	nb_img_loaded : 0,

	/*
	 * Fonction d'initalisation.
	 * Point d'entrée du viewer.
	 */
	init : function() {
		$(document).ready(function() {
			console.log("Document ready : starting application.");
			// Set screen size.
			viewer.width = window.screen.width;
			viewer.height = window.screen.height - 1;
			console.log("Screen size : ", viewer.width, " - ", viewer.height);
			// Load the viewer - for the first time
			viewer.reload();
			// Start a timer for future reloading.
			new LoopTimer(function(){
				viewer.reload();
			}, 10000);
		});
	},

	/*
	 * Get config file and configure the viewer.
	 */
	reload : function() {
		console.log('-----> Reloading viewer.')
		// Request the config file
		console.log('Config file - Requesting :', viewer.config_url);
		$.get(viewer.config_url, function(config, status, jqXHR) {
			console.log('Config file received : ' + config);
			// Update attrs.
			if (config != undefined) {
				// Check if timestamp change and so,
				// if there are modfications.
				console.log('Check if modifications ....');
				if (config.timestamp != viewer.timestamp) {
					console.log('Timestamp has changed -> reloading...');
					viewer.timestamp = config.timestamp;
					viewer.opts = config.opts;
					// Clear viewer
					viewer.clear();
					// Adding slides - with preloading
					viewer.preload(config.files);
				}else{
					console.log('No updates.')
				}
			}
		});
		console.log('---- End of reloading method.');
	},

	/*
	 * Run viewer animation.http://bigfarm.goodgamestudios.com/
	 */
	start : function() {
		$.each(viewer.images, function(index, img){
			img.attr('height', viewer.height);
			$(viewer.id_slideshow).append(img);
		});
		console.log('Starting viewer with args : ', viewer.opts);
		$(viewer.id_slideshow).cycle(viewer.opts);
	},

	/*
	 * Clear the viewer.
	 */
	clear : function() {
		console.log("Clearing viewer.");
		// Unbind events
		$(viewer.id_slideshow).cycle('destroy');
		// Clear imgs
		$(viewer.id_slideshow).empty();
	},

	/*
	 * Add a new slide into the viewer.
	 */
	add_slide : function(img) {
		console.log('Adding slide : ' + file_path);
		$(viewer.id_slideshow).append('<img class="slide" src="' + file_path + '" height="' + viewer.height + '" />');
	},

	/*
	 * Preloading images
	 */
	preload : function(images_path) {
		viewer.images = [];
		viewer.nb_img_loaded = 0;
		viewer.nb_img_to_load = images_path.length;
		$.each(images_path, function(index, path) {
			var new_img = $('<img />');
			new_img.attr('src', path);
			viewer.images[index] = new_img;
			new_img.load(function() {
				viewer.nb_img_loaded += 1;
				console.log('Image loaded : ', this);
				if(viewer.nb_img_to_load == viewer.nb_img_loaded){
					viewer.start();
				}
			});
		});
	}
};
