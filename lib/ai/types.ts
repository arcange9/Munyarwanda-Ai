export type Role='system'|'user'|'assistant'
export interface ChatMessage{role:Role;content:string;timestamp?:string}
export interface ProviderConfig{apiKey?:string;baseUrl?:string;model:string}
export interface StreamChunk{text:string;done?:boolean;model?:string;usage?:{promptTokens?:number;completionTokens?:number;totalTokens?:number}}
export interface AIProvider{id:string;streamChat(messages:ChatMessage[],config:ProviderConfig,signal?:AbortSignal):AsyncGenerator<StreamChunk>}
export type Language='rw'|'en'|'mixed'
