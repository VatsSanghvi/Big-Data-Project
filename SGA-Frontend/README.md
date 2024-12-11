# Vite + TypeScript + React Project

Welcome to the project! This guide will walk you through the steps to set up and run the project, both for developers and non-developers.

## Table of Contents

1. [For Non-Technical Users](#for-non-technical-users)
   - Installation Instructions
   - Running the Project
2. [For Developers](#for-developers)
   - Prerequisites
   - Setup Instructions
   - Running the Project Locally
   - Building the Project
   - Troubleshooting

---

## For Non-Technical Users

### Installation Instructions

If you're a non-technical user and just want to run the project, follow these easy steps:

1. **Download and Install Node.js**:

   - First, you need to install [Node.js](https://nodejs.org/), which is required to run the project.
   - Download the latest LTS version (recommended for most users).

2. **Download and Install Yarn**:

   - Yarn is a package manager that we use instead of `npm`. To install it, follow these instructions:
     - **macOS/Linux**: Run the following command in your terminal:
       ```bash
       npm install -g yarn
       ```
     - **Windows**: You can download the installer from the [Yarn website](https://classic.yarnpkg.com/en/docs/install/#windows-stable).

3. **Download the Project**:

   - You can either:
     - Download the ZIP of the project from the repository, or
     - If the project is hosted on GitHub, you can clone it using a Git client (ask a developer to help if you're unsure).

   **Important**: If you're downloading the project from GitHub, you may need Git installed. If that's the case, please refer to the [Git installation guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

4. **Install Dependencies**:

   - After downloading the project files, you need to install the required libraries. To do this:
     - **Windows**: Open Command Prompt in the project folder and run:
       ```bash
       yarn install
       ```
     - **Mac/Linux**: Open Terminal in the project folder and run:
       ```bash
       yarn install
       ```

5. **Running the Project**:

   - Once the dependencies are installed, you can run the project:
     - **Windows**: In the Command Prompt, run:
       ```bash
       yarn dev
       ```
     - **Mac/Linux**: In Terminal, run:
       ```bash
       yarn dev
       ```

6. **Open the Project in Your Browser**:
   - After running the project, open a web browser and go to `http://localhost:5173`. You should see the app running.

### Troubleshooting

- If you see any errors or issues, try restarting your computer, or ask a developer to help you.

---

## For Developers

### Prerequisites

Before you start, you need to have the following installed:

1. **Node.js** (version 16 or later) - [Download Node.js](https://nodejs.org/)
2. **Yarn** (package manager) - [Install Yarn](https://classic.yarnpkg.com/en/docs/install/)

---

### Setup Instructions

1. **Clone the Repository**:

   - If you haven't already, clone the project to your local machine using Git:
     ```bash
     git clone https://github.com/your-username/your-project-name.git
     ```

2. **Navigate to Project Folder**:

   - Go to the directory where you cloned the project:
     ```bash
     cd your-project-name
     ```

3. **Install Dependencies**:

   - Run the following command to install all necessary dependencies:
     ```bash
     yarn install
     ```

4. **Ensure TypeScript and Vite are Installed**:
   - Yarn should automatically handle all dependencies, but you can verify Vite and TypeScript installations:
     ```bash
     yarn list vite
     yarn list typescript
     ```

---

### Running the Project Locally

1. **Start the Development Server**:

   - Run the following command to start the local development server:
     ```bash
     yarn dev
     ```
   - This will start the app on `http://localhost:5173` (or another port, if configured).

2. **Open in Browser**:

   - Open your browser and navigate to `http://localhost:5173`. The app should load.

3. **Hot Reloading**:
   - Vite provides hot reloading, so any changes made to the code will automatically update in the browser without needing a manual refresh.

---

### Building the Project for Production

To create a production build, run the following command:

```bash
yarn build
```

This will generate an optimized version of the app in the `dist` folder.

- To preview the build locally, you can run:
  ```bash
  yarn preview
  ```

The app will be served at `http://localhost:5173` (or another port, if configured).

---

### Troubleshooting

1. **Missing dependencies**:

   - If you encounter issues related to missing packages, run:
     ```bash
     yarn install
     ```

2. **Outdated packages**:

   - To update the project's dependencies, run:
     ```bash
     yarn upgrade
     ```

3. **Vite or TypeScript Errors**:
   - If you see any build or TypeScript errors, check the error messages carefully. Often, the issue will be related to incorrect syntax or missing files.
   - If you're unsure about the error, consult the [Vite documentation](https://vitejs.dev/) or the [TypeScript documentation](https://www.typescriptlang.org/).

---

### Conclusion

That's it! You're all set up to work with this Vite + TypeScript + React project using Yarn. If you have any questions or run into issues, feel free to reach out or check the respective documentation.

Happy coding!

---

# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules:

- Configure the top-level `parserOptions` property like this:

```js
export default tseslint.config({
  languageOptions: {
    // other options...
    parserOptions: {
      project: ["./tsconfig.node.json", "./tsconfig.app.json"],
      tsconfigRootDir: import.meta.dirname,
    },
  },
});
```

- Replace `tseslint.configs.recommended` to `tseslint.configs.recommendedTypeChecked` or `tseslint.configs.strictTypeChecked`
- Optionally add `...tseslint.configs.stylisticTypeChecked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and update the config:

```js
// eslint.config.js
import react from "eslint-plugin-react";

export default tseslint.config({
  // Set the react version
  settings: { react: { version: "18.3" } },
  plugins: {
    // Add the react plugin
    react,
  },
  rules: {
    // other rules...
    // Enable its recommended rules
    ...react.configs.recommended.rules,
    ...react.configs["jsx-runtime"].rules,
  },
});
```
