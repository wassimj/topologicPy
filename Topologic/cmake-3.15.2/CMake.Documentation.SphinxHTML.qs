// Component: CMake.Documentation.SphinxHTML

function Component()
{
    // Default constructor
}

Component.prototype.createOperations = function()
{
    // Create shortcut
    if (installer.value("os") === "win") {

        component.addOperation("CreateShortcut",
                               "@TargetDir@/doc/cmake-3.15/html/index.html",
                               "@StartMenuDir@/CMake Documentation.lnk");

    }

    // Call default implementation
    component.createOperations();
}
