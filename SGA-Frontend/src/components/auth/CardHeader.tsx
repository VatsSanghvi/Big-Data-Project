export const CardHeader = ({ title }: CardHeaderProps) => {
    return (
        <div className="card-header">
            <h1>{title}</h1>
        </div>
    )
}

interface CardHeaderProps {
    title: string;
}