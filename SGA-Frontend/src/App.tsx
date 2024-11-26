// * React Libraries
import { createBrowserRouter, RouterProvider } from "react-router-dom";

// * Routes
import { routes } from "@routes";

export const App = () => {

    return (
        <RouterProvider router={createBrowserRouter(routes)}/>
    )
}
